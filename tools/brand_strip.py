"""First Mate brand strip for social images (content standard v2).

Usage: python3 brand_strip.py <fonts_dir> <src.jpg> [<src2.jpg> ...]
Writes <name>_v2.jpg next to each source. Images are 1080x1350 with the
FIRST MATE wordmark area at the bottom (y 1185-1340), which is repainted.
Fonts (Google Fonts, OFL): CormorantGaramond[wght].ttf,
CormorantGaramond-Italic[wght].ttf, JosefinSans[wght].ttf.
Carousel PDF: img2pdf p1_v2.jpg p2_v2.jpg ... -o FirstMate_<day>_carousel_v2.pdf
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont

def font(d, n, s, w):
    f = ImageFont.truetype(os.path.join(d, n), s)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f

def strip(fd, src, dst):
    im = Image.open(src).convert("RGB"); d = ImageDraw.Draw(im)
    bg = im.getpixel((540, 1170)); d.rectangle([120, 1185, 960, 1340], fill=bg)
    def sp(t, f, y, col, gap):
        w = sum(d.textlength(c, font=f) + gap for c in t) - gap; x = (1080 - w) / 2
        for c in t: d.text((x, y), c, font=f, fill=col); x += d.textlength(c, font=f) + gap
    sp("FIRST MATE", font(fd, "CormorantGaramond[wght].ttf", 50, 500), 1188, (250, 246, 238), 12)
    sp("PRINTABLE PLANNERS & TEMPLATES", font(fd, "JosefinSans[wght].ttf", 21, 600), 1252, (88, 200, 170), 5)
    f = font(fd, "CormorantGaramond-Italic[wght].ttf", 34, 500); t = "Pick your priorities. Check them every day."
    d.text(((1080 - d.textlength(t, font=f)) / 2, 1284), t, font=f, fill=(240, 160, 40))
    im.save(dst, quality=95)

if __name__ == "__main__":
    fd = sys.argv[1]
    for s in sys.argv[2:]: strip(fd, s, s.replace(".jpg", "_v2.jpg"))
