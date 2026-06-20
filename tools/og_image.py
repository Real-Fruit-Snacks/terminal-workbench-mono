"""Generate docs/og-image.png (social card) and docs/favicon.png from the font."""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
TTF = os.path.join(ROOT, 'dist', 'ttf')
DOCS = os.path.join(ROOT, 'docs')
BG = (11, 16, 24)
PANEL = (16, 23, 36)
FG = (223, 231, 239)
ACCENT = (126, 211, 211)
DIM = (130, 145, 160)
GREEN = (157, 223, 157)


def font(style, px):
    return ImageFont.truetype(os.path.join(TTF, f'ShellbackMono-{style}.ttf'), px)


def og_card():
    W, H = 1200, 630
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    # faint scanline texture
    for y in range(0, H, 4):
        d.line([(0, y), (W, y)], fill=(14, 20, 30), width=1)
    d.rectangle([0, 0, 14, H], fill=ACCENT)

    d.text((70, 96), "Shellback Mono", font=font('Bold', 96), fill=FG)
    d.text((74, 214), "a water-cooled monospace", font=font('Regular', 40), fill=DIM)

    d.text((74, 320), "0O Il1 5S 8B", font=font('Medium', 60), fill=ACCENT)
    d.text((74, 404), "-> <- => != == <= >=", font=font('Regular', 46), fill=GREEN)
    d.text((74, 486), "for security notes · terminals · Obsidian",
           font=font('Regular', 34), fill=DIM)
    img.save(os.path.join(DOCS, 'og-image.png'))
    print('wrote docs/og-image.png')


def favicon():
    S = 256
    img = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([8, 8, S - 8, S - 8], radius=48, fill=PANEL,
                        outline=ACCENT, width=10)
    f = font('Bold', 210)
    # center the S in the rounded square
    box = d.textbbox((0, 0), "S", font=f)
    w, h = box[2] - box[0], box[3] - box[1]
    d.text(((S - w) / 2 - box[0], (S - h) / 2 - box[1]), "S", font=f, fill=ACCENT)
    img.save(os.path.join(DOCS, 'favicon.png'))
    print('wrote docs/favicon.png')


if __name__ == '__main__':
    og_card()
    favicon()
