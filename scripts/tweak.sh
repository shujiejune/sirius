# Adjust the glyph
uv run --with fonttools --with brotli python scripts/font-tweak.py \
    src/assets/fonts/full/ZillaSlab-Regular.woff2 --target-xh 50 \
    --output src/assets/fonts/ZillaSlab-Regular.woff2

# Widen word spacing
uv run --with fonttools --with brotli python scripts/font-tweak.py \
    src/assets/fonts/ZillaSlab-Regular.woff2 --word-space 1.08
