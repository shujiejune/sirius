#!/usr/bin/env python3
"""
Subset the full CJK fonts in src/assets/fonts/full/ to only the characters
actually used by the site, writing the slim woff2 files back to
src/assets/fonts/ under their original names (the @font-face urls stay valid).

Character set = every character found in src/content/** (posts) and
src/**/*.astro / src/consts.* (UI strings), plus ASCII/Latin-1, CJK and
fullwidth punctuation blocks, so metadata and future light edits are covered.

Rerun this after publishing posts that use new characters:

    uv run --with fonttools --with brotli python scripts/subset-fonts.py
"""

import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FULL_DIR = ROOT / "src" / "assets" / "fonts" / "full"
OUT_DIR = ROOT / "src" / "assets" / "fonts"

# Fixed additions beyond the scanned text: punctuation and symbols that
# markdown rendering or future copy could inject.
EXTRA_RANGES = [
    range(0x0020, 0x0250),   # ASCII + Latin-1 Supplement + Latin Extended-A/B
    range(0x2000, 0x2070),   # General Punctuation (dashes, quotes, ellipsis, …)
    range(0x3000, 0x3040),   # CJK Symbols and Punctuation (「」『』、。〈〉《》…)
    range(0xFF01, 0xFF66),   # Fullwidth forms (，！？：；(etc.) + halfwidth katakana)
    range(0x2E80, 0x2EF0),   # CJK Radicals Supplement (occasionally quoted)
    range(0x2F00, 0x2FD6),   # Kangxi Radicals
    range(0x31C0, 0x31F0),   # CJK Strokes
]

def collect_chars() -> set[int]:
    chars: set[int] = set()
    for cp in EXTRA_RANGES:
        chars.update(cp)
    sources = list((ROOT / "src" / "content").rglob("*.[mdx][dm]*"))
    sources = [p for p in sources if p.suffix in (".md", ".mdx")]
    sources += list((ROOT / "src").rglob("*.astro"))
    for pattern in ("src/consts.ts", "src/consts.js"):
        p = ROOT / pattern
        if p.exists():
            sources.append(p)
    for path in sources:
        chars.update(ord(c) for c in path.read_text(encoding="utf-8"))
    return chars

def subset_font(src: Path, dst: Path, text_file: Path) -> tuple[int, int]:
    args = [
        str(src),
        f"--text-file={text_file}",
        f"--output-file={dst}",
        "--flavor=woff2",
        "--no-hinting",
        "--drop-tables+=DSIG",
        "--name-IDs=*",
    ]
    subset.main(args)
    return src.stat().st_size, dst.stat().st_size

def coverage(full_paths: list[Path], sub_paths: list[Path], chars: set[int]) -> set[int]:
    """Report characters present in the full fonts but dropped by subsetting
    (control chars and glyphs the full fonts never had are not a problem)."""
    def cmap_union(paths: list[Path]) -> set[int]:
        covered: set[int] = set()
        for p in paths:
            covered.update(TTFont(p).getBestCmap().keys())
        return covered

    chars = {c for c in chars if c >= 0x20 and c != 0x7F}  # skip control chars
    in_full = cmap_union(full_paths)
    in_sub = cmap_union(sub_paths)
    return (chars & in_full) - in_sub

def main() -> int:
    chars = collect_chars()
    print(f"charset: {len(chars)} unique codepoints from {len(EXTRA_RANGES)} fixed ranges + scanned sources")

    text_file = FULL_DIR / ".charset.txt"
    text_file.write_text("".join(chr(c) for c in sorted(chars)), encoding="utf-8")

    outputs = []
    for src in sorted(FULL_DIR.glob("*.woff2")):
        dst = OUT_DIR / src.name
        before, after = subset_font(src, dst, text_file)
        outputs.append(dst)
        print(f"  {src.name}: {before/1e6:.2f} MB -> {after/1e6:.2f} MB")

    text_file.unlink()

    missing = coverage(sorted(FULL_DIR.glob("*.woff2")), outputs, chars)
    if missing:
        sample = "".join(chr(c) for c in sorted(missing)[:40])
        print(f"WARNING: {len(missing)} chars exist in full fonts but were dropped "
              f"from the subsets (browser will fall back): {sample}")
        return 1
    print("coverage OK: nothing that the full fonts provide was lost")
    return 0

if __name__ == "__main__":
    sys.exit(main())
