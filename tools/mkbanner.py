#!/usr/bin/env python3
# Kompaktny VLAJKA-VIEWER banner (pomer ~2,8; sirka 3,6 cm) — PNG pre vlozenie do DOCX klonu
from PIL import Image, ImageDraw, ImageFont
import glob, os

W, H = 425, 152                       # 3,6 cm x 1,29 cm pri 300 dpi
NAME = {"FR":"FRANÇAIS","HR":"HRVATSKI","PL":"POLSKI","IT":"ITALIANO","ES":"ESPAÑOL","SV":"SVENSKA"}

def font(bold, size):
    pats = ["/usr/share/fonts/truetype/crosextra/Carlito-%s.ttf" % ("Bold" if bold else "Regular"),
            "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else "")]
    for p in pats:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def flag(code, w, h):
    im = Image.new("RGB", (w, h), "white"); d = ImageDraw.Draw(im)
    if code == "FR":
        d.rectangle([0,0,w//3,h], fill="#0055A4"); d.rectangle([w//3,0,2*w//3,h], fill="#FFFFFF"); d.rectangle([2*w//3,0,w,h], fill="#EF4135")
    elif code == "IT":
        d.rectangle([0,0,w//3,h], fill="#009246"); d.rectangle([w//3,0,2*w//3,h], fill="#FFFFFF"); d.rectangle([2*w//3,0,w,h], fill="#CE2B37")
    elif code == "PL":
        d.rectangle([0,0,w,h//2], fill="#FFFFFF"); d.rectangle([0,h//2,w,h], fill="#DC143C")
    elif code == "ES":
        d.rectangle([0,0,w,h], fill="#AA151B"); d.rectangle([0,h//4,w,3*h//4], fill="#F1BF00")
    elif code == "HR":
        d.rectangle([0,0,w,h//3], fill="#FF0000"); d.rectangle([0,h//3,w,2*h//3], fill="#FFFFFF"); d.rectangle([0,2*h//3,w,h], fill="#171796")
        cx, cy, cw, ch = w//2-w//10, h//3-h//8, w//5, h//2          # zjednoduseny grb
        d.rectangle([cx,cy,cx+cw,cy+ch], fill="#FFFFFF", outline="#171796")
        sq = cw//4
        for iy in range(4):
            for ix in range(4):
                if (ix+iy) % 2 == 0:
                    d.rectangle([cx+ix*sq, cy+iy*(ch//4), cx+(ix+1)*sq, cy+(iy+1)*(ch//4)], fill="#FF0000")
    elif code == "SV":
        d.rectangle([0,0,w,h], fill="#005293")
        d.rectangle([int(w*0.30),0,int(w*0.44),h], fill="#FECB00")
        d.rectangle([0,int(h*0.40),w,int(h*0.60)], fill="#FECB00")
    return im

def build(code, out):
    im = Image.new("RGBA", (W, H), (255,255,255,255))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([2,2,W-3,H-3], radius=16, outline="#E4002B", width=5)
    fw, fh = 96, 64
    fl = flag(code, fw, fh)
    im.paste(fl, (20, (H-fh)//2))
    d.rectangle([20,(H-fh)//2,20+fw,(H-fh)//2+fh], outline="#999999", width=2)
    tx = 20 + fw + 18
    fb = font(True, 46); fs = font(False, 19)
    name = NAME[code]
    while d.textlength(name, font=fb) > W - tx - 22 and fb.size > 22:
        fb = font(True, fb.size - 2)
    d.text((tx, 32), name, font=fb, fill="#111111")
    d.text((tx, 96), "VLAJKA-VIEWER · " + code, font=fs, fill="#333333")
    im.convert("RGB").save(out)
    print("banner:", out, im.size)

if __name__ == "__main__":
    import sys
    build(sys.argv[1], sys.argv[2])
