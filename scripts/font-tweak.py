#!/usr/bin/env python3
"""Tweak a font file: rescale its design grid and/or widen word spacing.

Run from the repo root with uv (fetches fonttools + brotli automatically):

  uv run --with fonttools --with brotli python scripts/font-tweak.py <font> \
      [--target-xh 50] [--word-space 1.15] [--output <out>]

--target-xh   Target x-height as a percentage of the em (e.g. 50 = 50%).
              Recalculates unitsPerEm so the font's x-height lands on this
              value. Bigger % = larger glyphs at the same CSS font-size.
              Zilla Slab original: ~44.5. Hanuman: ~53.6.
--word-space  Multiply the advance width of the space (U+0020) and
              no-break space (U+00A0) glyphs by this factor. 1.15 = 15%
              wider word gaps.

Always start from the ORIGINAL fonts in src/assets/fonts/full/ and write
to src/assets/fonts/ — re-scaling an already-scaled file compounds.
"""

import argparse

from fontTools.ttLib import TTFont

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("font", help="input font (.woff2 or .ttf)")
parser.add_argument("--target-xh", type=float, help="target x-height %% of em")
parser.add_argument("--word-space", type=float, help="space advance multiplier")
parser.add_argument("--output", help="output path (default: overwrite input)")
args = parser.parse_args()

if not (args.target_xh or args.word_space):
    parser.error("nothing to do: pass --target-xh and/or --word-space")

font = TTFont(args.font)
head, os2 = font["head"], font["OS/2"]

if args.target_xh:
    xh = os2.sxHeight
    new_upm = round(xh / (args.target_xh / 100))
    head.unitsPerEm = new_upm
    print(f"grid: upm {new_upm}, x-height now {xh / new_upm * 100:.1f}% of em")

if args.word_space:
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]
    for cp in (0x20, 0xA0):  # space, no-break space
        glyph = cmap.get(cp)
        if glyph:
            width, lsb = hmtx[glyph]
            hmtx[glyph] = (round(width * args.word_space), lsb)
            print(
                f"space U+{cp:04X}: advance {width} -> "
                f"{round(width * args.word_space)} units"
            )

out = args.output or args.font
font.save(out)
print(f"saved: {out}")
