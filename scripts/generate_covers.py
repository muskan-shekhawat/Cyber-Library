#!/usr/bin/env python3
"""
Generate 24 clean, museum-grade Swiss/editorial cybersecurity book cover artworks (800x1200, 2:3).
Each cover has a dedicated quiet upper/lower typographic region and bold subject-specific
geometric artwork below, so HTML/CSS Inter typography integrates seamlessly without opaque boxes.
"""

import math
import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "public/images/books"
os.makedirs(OUTPUT_DIR, exist_ok=True)

W, H = 800, 1200


def new_canvas(bg):
    return Image.new("RGB", (W, H), bg)


def draw_circle(draw, cx, cy, r, fill=None, outline=None, width=1):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill, outline=outline, width=width)


# 01. Computer Networking Fundamentals — Cobalt Blue & Warm Coral on Crisp Cream
def gen_computer_networking():
    img = new_canvas((247, 245, 240))
    d = ImageDraw.Draw(img)
    # Subtle grid in lower artwork region
    for x in range(80, W - 60, 64):
        d.line([(x, 420), (x, 1080)], fill=(230, 227, 220), width=1)
    for y in range(420, 1100, 64):
        d.line([(60, y), (W - 60, y)], fill=(230, 227, 220), width=1)

    cx, cy = 400, 760
    draw_circle(d, cx, cy, 240, outline=(37, 99, 235), width=4)
    draw_circle(d, cx, cy, 155, outline=(249, 115, 22), width=4)
    draw_circle(d, cx, cy, 78, fill=(37, 99, 235))

    nodes = []
    for i in range(8):
        a = i * (2 * math.pi / 8) + 0.35
        nx, ny = int(cx + 240 * math.cos(a)), int(cy + 240 * math.sin(a))
        nodes.append((nx, ny))
        d.line([(cx, cy), (nx, ny)], fill=(30, 58, 138), width=3)

    for i, (nx, ny) in enumerate(nodes):
        col = (249, 115, 22) if i % 2 == 0 else (37, 99, 235)
        draw_circle(d, nx, ny, 22, fill=(247, 245, 240), outline=col, width=5)
        draw_circle(d, nx, ny, 9, fill=col)

    d.rectangle([72, 340, 210, 348], fill=(249, 115, 22))
    return img


# 02. Advanced Networking — Deep Cobalt & Cyan Isometric Layers
def gen_advanced_networking():
    img = new_canvas((20, 48, 108))
    d = ImageDraw.Draw(img)
    layers = [
        (560, (56, 189, 248)),
        (710, (37, 99, 235)),
        (860, (245, 158, 11)),
    ]
    for yc, col in layers:
        pts = [(400, yc - 95), (670, yc - 10), (400, yc + 75), (130, yc - 10)]
        d.polygon(pts, fill=col)
        d.line([(400, yc - 95), (400, yc + 75)], fill=(255, 255, 255), width=2)
        d.line([(130, yc - 10), (670, yc - 10)], fill=(255, 255, 255), width=2)

    for x in [265, 400, 535]:
        d.line([(x, 465), (x, 940)], fill=(255, 255, 255), width=3)
        for y in [550, 700, 850]:
            draw_circle(d, x, y, 8, fill=(20, 48, 108), outline=(255, 255, 255), width=3)
    return img


# 03. Linux Fundamentals — Warm Terracotta & Graphite Terminal Rings
def gen_linux_fundamentals():
    img = new_canvas((252, 245, 232))
    d = ImageDraw.Draw(img)
    d.rectangle([80, 460, 720, 1060], fill=(28, 35, 49))
    d.rectangle([80, 460, 720, 514], fill=(15, 23, 42))
    for i, col in enumerate([(239, 68, 68), (245, 158, 11), (16, 185, 129)]):
        draw_circle(d, 116 + i * 28, 487, 7, fill=col)

    cx, cy = 400, 785
    draw_circle(d, cx, cy, 170, outline=(245, 158, 11), width=4)
    draw_circle(d, cx, cy, 110, outline=(251, 191, 36), width=3)
    draw_circle(d, cx, cy, 52, fill=(217, 119, 6))
    d.polygon([(cx - 14, cy - 18), (cx + 18, cy), (cx - 14, cy + 18)], fill=(252, 245, 232))
    d.rectangle([80, 340, 180, 348], fill=(217, 119, 6))
    return img


# 04. Kali Linux Handbook — Royal Indigo & Electric Cyan Polygon Crest
def gen_kali_linux():
    img = new_canvas((30, 27, 75))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    p1 = [(cx, cy - 240), (cx + 210, cy - 55), (cx + 150, cy + 170), (cx, cy + 240), (cx - 150, cy + 170), (cx - 210, cy - 55)]
    d.polygon(p1, fill=(67, 56, 202))
    p2 = [(cx, cy - 175), (cx + 145, cy - 35), (cx + 100, cy + 120), (cx, cy + 175), (cx - 100, cy + 120), (cx - 145, cy - 35)]
    d.polygon(p2, fill=(79, 70, 229))
    p3 = [(cx, cy - 110), (cx + 75, cy - 15), (cx, cy + 105), (cx - 75, cy - 15)]
    d.polygon(p3, fill=(6, 182, 212))
    d.line([(cx, cy - 280), (cx, cy + 280)], fill=(129, 140, 248), width=2)
    d.line([(cx - 280, cy), (cx + 280, cy)], fill=(129, 140, 248), width=2)
    draw_circle(d, cx, cy, 265, outline=(99, 102, 241), width=2)
    return img


# 05. Linux System Administration — Spruce Teal & Jade Server Architecture
def gen_linux_administration():
    img = new_canvas((15, 82, 76))
    d = ImageDraw.Draw(img)
    for rx in [120, 315, 510]:
        d.rectangle([rx, 500, rx + 170, 1040], fill=(13, 118, 108))
        for i in range(6):
            by = 524 + i * 82
            d.rectangle([rx + 16, by, rx + 154, by + 58], fill=(20, 148, 134))
            led = (250, 204, 21) if i % 3 == 0 else (167, 243, 208)
            draw_circle(d, rx + 34, by + 29, 6, fill=led)
            d.line([(rx + 56, by + 29), (rx + 138, by + 29)], fill=(204, 251, 241), width=4)
    d.arc([160, 410, 640, 590], start=180, end=0, fill=(250, 204, 21), width=5)
    return img


# 06. Ethical Hacking Fundamentals — Bold Vermilion & Ivory Target Shield
def gen_ethical_hacking():
    img = new_canvas((252, 242, 242))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    draw_circle(d, cx, cy, 245, fill=(225, 29, 72))
    draw_circle(d, cx, cy, 180, fill=(244, 63, 94))
    draw_circle(d, cx, cy, 115, fill=(252, 242, 242))
    d.polygon([(cx, cy - 75), (cx + 58, cy + 50), (cx - 58, cy + 50)], fill=(136, 19, 55))
    draw_circle(d, cx, cy - 55, 24, fill=(136, 19, 55))
    for a in range(0, 360, 45):
        rad = math.radians(a)
        d.line([(cx + int(255 * math.cos(rad)), cy + int(255 * math.sin(rad))),
                (cx + int(282 * math.cos(rad)), cy + int(282 * math.sin(rad)))], fill=(225, 29, 72), width=4)
    d.rectangle([72, 340, 190, 348], fill=(225, 29, 72))
    return img


# 07. Penetration Testing — Vibrant Tangerine & Charcoal Wedge
def gen_penetration_testing():
    img = new_canvas((234, 88, 12))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    draw_circle(d, cx, cy, 250, fill=(249, 115, 22))
    draw_circle(d, cx, cy, 185, fill=(251, 146, 60))
    draw_circle(d, cx, cy, 115, fill=(255, 247, 237))
    d.polygon([(80, cy - 95), (cx + 75, cy), (80, cy + 95)], fill=(24, 24, 27))
    for ang in [-35, -18, 0, 18, 35]:
        r = math.radians(ang)
        d.line([(cx + 75, cy), (cx + 75 + int(160 * math.cos(r)), cy + int(160 * math.sin(r)))], fill=(234, 88, 12), width=4)
    draw_circle(d, cx + 75, cy, 10, fill=(255, 255, 255))
    return img


# 08. Web Application Security — Crisp White, Ultramarine & Mint Browser Planes
def gen_web_security():
    img = new_canvas((242, 246, 252))
    d = ImageDraw.Draw(img)
    frames = [
        (90, 480, 500, 360, (37, 99, 235)),
        (145, 570, 500, 360, (16, 185, 129)),
        (200, 660, 510, 360, (255, 255, 255)),
    ]
    for x, y, w, h, col in frames:
        d.rectangle([x, y, x + w, y + h], fill=col, outline=(30, 41, 59), width=2)
        d.rectangle([x, y, x + w, y + 36], fill=(30, 41, 59))
        for i, c in enumerate([(239, 68, 68), (245, 158, 11), (16, 185, 129)]):
            draw_circle(d, x + 22 + i * 20, y + 18, 5, fill=c)

    px, py = 455, 845
    d.rectangle([px - 42, py, px + 42, py + 66], fill=(37, 99, 235))
    d.arc([px - 30, py - 46, px + 30, py + 14], start=180, end=0, fill=(37, 99, 235), width=9)
    draw_circle(d, px, py + 30, 8, fill=(255, 255, 255))
    d.rectangle([72, 340, 200, 348], fill=(37, 99, 235))
    return img


# 09. OWASP Top 10 — Multi-Colour Swiss Bauhaus Ten Pillars
def gen_owasp_top10():
    img = new_canvas((248, 247, 244))
    d = ImageDraw.Draw(img)
    colors = [
        (244, 63, 94), (249, 115, 22), (245, 158, 11), (132, 204, 22),
        (16, 185, 129), (20, 184, 166), (14, 165, 233), (59, 130, 246),
        (139, 92, 246), (217, 70, 239)
    ]
    bw = 54
    sx = 94
    for i, col in enumerate(colors):
        x = sx + i * 62
        h = 200 + ((i * 73) % 280)
        y = 1010 - h
        d.rectangle([x, y, x + bw, 1010], fill=col)
        draw_circle(d, x + bw // 2, y - 34, 15, fill=col)
    d.line([(72, 1010), (728, 1010)], fill=(34, 34, 34), width=5)
    d.rectangle([72, 340, 220, 348], fill=(244, 63, 94))
    return img


# 10. Python for Cybersecurity — Prussian Blue & Golden Topaz Interlocking Loops
def gen_python_cybersecurity():
    img = new_canvas((23, 37, 84))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    d.arc([cx - 190, cy - 220, cx + 70, cy + 40], start=90, end=360, fill=(56, 189, 248), width=36)
    d.rectangle([cx - 55, cy - 220, cx + 110, cy - 125], fill=(56, 189, 248))
    draw_circle(d, cx + 52, cy - 172, 12, fill=(23, 37, 84))

    d.arc([cx - 70, cy - 40, cx + 190, cy + 220], start=270, end=180, fill=(250, 204, 21), width=36)
    d.rectangle([cx - 110, cy + 125, cx + 55, cy + 220], fill=(250, 204, 21))
    draw_circle(d, cx - 52, cy + 172, 12, fill=(23, 37, 84))

    for a in range(30, 360, 60):
        r = math.radians(a)
        draw_circle(d, int(cx + 265 * math.cos(r)), int(cy + 265 * math.sin(r)), 12, fill=(45, 212, 191))
    return img


# 11. Bash Scripting — Slate Graphite & Chartreuse Pipeline Streams
def gen_bash_scripting():
    img = new_canvas((24, 31, 44))
    d = ImageDraw.Draw(img)
    d.line([(100, 620), (700, 620)], fill=(132, 204, 22), width=6)
    d.line([(100, 760), (700, 760)], fill=(6, 182, 212), width=6)
    d.line([(100, 900), (700, 900)], fill=(245, 158, 11), width=6)
    d.rectangle([384, 520, 416, 1000], fill=(248, 250, 252))
    d.polygon([(475, 695), (565, 760), (475, 825)], fill=(132, 204, 22))
    d.polygon([(325, 695), (235, 760), (325, 825)], fill=(6, 182, 212))
    return img


# 12. OSINT Field Guide — Soft Lavender & Iris Constellation Reticle
def gen_osint_guide():
    img = new_canvas((243, 240, 252))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    draw_circle(d, cx, cy, 230, outline=(124, 58, 237), width=5)
    draw_circle(d, cx, cy, 165, fill=(233, 226, 254))
    d.line([(cx - 255, cy), (cx + 255, cy)], fill=(167, 139, 250), width=2)
    d.line([(cx, cy - 255), (cx, cy + 255)], fill=(167, 139, 250), width=2)
    pts = [(cx - 95, cy - 85), (cx + 115, cy - 65), (cx + 75, cy + 85),
           (cx - 75, cy + 95), (cx, cy - 135), (cx - 135, cy + 10), (cx + 135, cy + 20)]
    for p1 in pts:
        for p2 in pts:
            if p1 != p2:
                d.line([p1, p2], fill=(167, 139, 250), width=2)
    for px, py in pts:
        draw_circle(d, px, py, 12, fill=(124, 58, 237), outline=(255, 255, 255), width=3)
    d.rectangle([72, 340, 180, 348], fill=(124, 58, 237))
    return img


# 13. Wireshark Network Analysis — Ocean Azure & Seafoam Packet Waves
def gen_wireshark():
    img = new_canvas((236, 246, 254))
    d = ImageDraw.Draw(img)
    d.polygon([(200, 960), (390, 490), (580, 780), (510, 960)], fill=(2, 132, 199))
    d.polygon([(260, 960), (410, 580), (545, 825), (485, 960)], fill=(12, 74, 110))
    for wy, col in [(660, (20, 184, 166)), (760, (56, 189, 248)), (860, (244, 63, 94))]:
        pts = [(x, wy + int(28 * math.sin((x - 80) * 0.022))) for x in range(80, 721, 10)]
        for i in range(len(pts) - 1):
            d.line([pts[i], pts[i + 1]], fill=col, width=4)
    d.rectangle([72, 340, 200, 348], fill=(2, 132, 199))
    return img


# 14. Nmap Network Scanning — Safety Orange Polar Radar on Warm Paper
def gen_nmap():
    img = new_canvas((254, 244, 234))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    for r in [70, 140, 210, 280]:
        draw_circle(d, cx, cy, r, outline=(249, 115, 22), width=2)
    d.line([(cx - 280, cy), (cx + 280, cy)], fill=(249, 115, 22), width=2)
    d.line([(cx, cy - 280), (cx, cy + 280)], fill=(249, 115, 22), width=2)
    d.pieslice([cx - 280, cy - 280, cx + 280, cy + 280], start=295, end=345, fill=(251, 146, 60))
    for bx, by in [(cx + 110, cy - 125), (cx - 75, cy - 140), (cx + 165, cy + 80), (cx - 170, cy + 105)]:
        draw_circle(d, bx, by, 13, fill=(234, 88, 12), outline=(255, 255, 255), width=3)
    d.rectangle([72, 340, 190, 348], fill=(234, 88, 12))
    return img


# 15. Digital Forensics — Warm Stone & Terracotta Fingerprint Ridges
def gen_digital_forensics():
    img = new_canvas((245, 243, 238))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    for r in range(40, 260, 24):
        d.arc([cx - int(r * 0.8), cy - r, cx + int(r * 0.8), cy + r], start=25, end=250, fill=(30, 41, 59), width=5)
        d.arc([cx - int(r * 0.8), cy - r, cx + int(r * 0.8), cy + r], start=275, end=358, fill=(194, 65, 12), width=5)
    d.rectangle([cx - 150, cy - 150, cx + 150, cy + 150], outline=(194, 65, 12), width=4)
    d.rectangle([72, 340, 190, 348], fill=(194, 65, 12))
    return img


# 16. Cryptography — Deep Amethyst & Gold Cipher Gear
def gen_cryptography():
    img = new_canvas((76, 29, 149))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    draw_circle(d, cx, cy, 245, fill=(107, 33, 168))
    for i in range(24):
        ang = i * (2 * math.pi / 24)
        draw_circle(d, int(cx + 258 * math.cos(ang)), int(cy + 258 * math.sin(ang)), 9, fill=(245, 158, 11))
    draw_circle(d, cx, cy, 170, fill=(147, 51, 234))
    draw_circle(d, cx, cy, 98, fill=(248, 244, 255))
    draw_circle(d, cx, cy - 16, 22, fill=(76, 29, 149))
    d.polygon([(cx - 14, cy), (cx + 14, cy), (cx + 24, cy + 46), (cx - 24, cy + 46)], fill=(76, 29, 149))
    return img


# 17. Malware Analysis — Charcoal & Ruby Hexagonal Quarantine
def gen_malware_analysis():
    img = new_canvas((24, 24, 27))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    pts = [(int(cx + 245 * math.cos(i * math.pi / 3 + math.pi / 6)),
            int(cy + 245 * math.sin(i * math.pi / 3 + math.pi / 6))) for i in range(6)]
    d.polygon(pts, fill=(63, 63, 70))
    pts2 = [(int(cx + 170 * math.cos(i * math.pi / 3 + math.pi / 6)),
             int(cy + 170 * math.sin(i * math.pi / 3 + math.pi / 6))) for i in range(6)]
    d.polygon(pts2, fill=(220, 38, 38))
    for p in pts:
        d.line([(cx, cy), p], fill=(244, 244, 245), width=2)
    draw_circle(d, cx, cy, 34, fill=(244, 244, 245))
    return img


# 18. Windows Security & AD — Clean Sky Blue Quad-Tile & Tree
def gen_windows_security():
    img = new_canvas((240, 247, 254))
    d = ImageDraw.Draw(img)
    cx, cy, s, g = 400, 680, 140, 20
    d.rectangle([cx - s - g // 2, cy - s - g // 2, cx - g // 2, cy - g // 2], fill=(2, 132, 199))
    d.rectangle([cx + g // 2, cy - s - g // 2, cx + s + g // 2, cy - g // 2], fill=(14, 165, 233))
    d.rectangle([cx - s - g // 2, cy + g // 2, cx - g // 2, cy + s + g // 2], fill=(56, 189, 248))
    d.rectangle([cx + g // 2, cy + g // 2, cx + s + g // 2, cy + s + g // 2], fill=(3, 105, 161))

    d.line([(cx, cy + s), (cx, 910)], fill=(71, 85, 105), width=4)
    d.line([(cx, 910), (cx - 150, 995)], fill=(71, 85, 105), width=4)
    d.line([(cx, 910), (cx + 150, 995)], fill=(71, 85, 105), width=4)
    for nx, ny in [(cx, 910), (cx - 150, 995), (cx + 150, 995)]:
        draw_circle(d, nx, ny, 18, fill=(245, 158, 11), outline=(30, 41, 59), width=3)
    d.rectangle([72, 340, 190, 348], fill=(2, 132, 199))
    return img


# 19. SOC Analyst Handbook — Deep Petrol & Emerald Telemetry Radar
def gen_soc_analyst():
    img = new_canvas((6, 54, 48))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    draw_circle(d, cx, cy, 240, fill=(13, 148, 136))
    draw_circle(d, cx, cy, 165, fill=(16, 185, 129))
    draw_circle(d, cx, cy, 90, fill=(167, 243, 208))
    d.line([(cx - 265, cy), (cx + 265, cy)], fill=(250, 204, 21), width=4)
    d.line([(cx, cy - 265), (cx, cy + 265)], fill=(250, 204, 21), width=4)
    draw_circle(d, cx, cy, 24, fill=(6, 54, 48))
    return img


# 20. Incident Response — Bold Coral Lifecycle Ring & Signal Crest
def gen_incident_response():
    img = new_canvas((254, 242, 242))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    phases = [
        (0, 62, (239, 68, 68)),
        (72, 134, (249, 115, 22)),
        (144, 206, (234, 179, 8)),
        (216, 278, (30, 58, 138)),
        (288, 350, (59, 130, 246)),
    ]
    for s_deg, e_deg, col in phases:
        d.arc([cx - 220, cy - 220, cx + 220, cy + 220], start=s_deg, end=e_deg, fill=col, width=28)
    draw_circle(d, cx, cy, 110, fill=(30, 58, 138))
    d.polygon([(cx + 10, cy - 60), (cx - 35, cy), (cx, cy), (cx - 15, cy + 60), (cx + 35, cy - 10), (cx, cy - 10)], fill=(250, 204, 21))
    d.rectangle([72, 340, 190, 348], fill=(239, 68, 68))
    return img


# 21. Cloud Security — Sky Azure & Indigo Cloud Strata
def gen_cloud_security():
    img = new_canvas((239, 246, 255))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    for x, y, r, col in [
        (cx - 145, cy + 35, 100, (56, 189, 248)),
        (cx + 145, cy + 35, 100, (56, 189, 248)),
        (cx - 80, cy - 45, 120, (79, 70, 229)),
        (cx + 75, cy - 35, 110, (99, 102, 241)),
        (cx, cy + 50, 130, (14, 165, 233)),
    ]:
        draw_circle(d, x, y, r, fill=col)
    d.rectangle([cx - 245, cy + 65, cx + 245, cy + 135], fill=(14, 165, 233))
    draw_circle(d, cx, cy + 10, 265, outline=(79, 70, 229), width=4)
    d.rectangle([72, 340, 190, 348], fill=(79, 70, 229))
    return img


# 22. API Security — Fuchsia & Violet Gateway Matrix
def gen_api_security():
    img = new_canvas((252, 243, 255))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    for p1, p2 in [((cx - 280, cy), (cx + 280, cy)), ((cx, cy - 280), (cx, cy + 280))]:
        d.line([p1, p2], fill=(139, 92, 246), width=8)
    d.rectangle([cx - 110, cy - 110, cx + 110, cy + 110], fill=(217, 70, 239))
    d.rectangle([cx - 46, cy - 46, cx + 46, cy + 46], fill=(255, 255, 255))
    for ex, ey in [(cx - 280, cy), (cx + 280, cy), (cx, cy - 280), (cx, cy + 280)]:
        draw_circle(d, ex, ey, 18, fill=(217, 70, 239), outline=(255, 255, 255), width=3)
    d.rectangle([72, 340, 190, 348], fill=(217, 70, 239))
    return img


# 23. Wireless Network Security — Teal & Coral Radio Wave Arcs
def gen_wireless_security():
    img = new_canvas((236, 253, 248))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 920
    for r in [110, 185, 260, 335, 410]:
        d.arc([cx - r, cy - r, cx + r, cy + r], start=205, end=335, fill=(13, 148, 136), width=10)
    draw_circle(d, cx, cy, 34, fill=(244, 63, 94))
    lx, ly = 400, 680
    d.rectangle([lx - 45, ly, lx + 45, ly + 68], fill=(244, 63, 94))
    d.arc([lx - 32, ly - 46, lx + 32, ly + 12], start=180, end=0, fill=(244, 63, 94), width=10)
    draw_circle(d, lx, ly + 32, 10, fill=(255, 255, 255))
    d.rectangle([72, 340, 190, 348], fill=(13, 148, 136))
    return img


# 24. Mobile Application Security — Clean Graphite & Violet Device Frame
def gen_mobile_security():
    img = new_canvas((245, 243, 255))
    d = ImageDraw.Draw(img)
    cx, cy = 400, 760
    d.rectangle([cx - 155, cy - 265, cx + 155, cy + 265], fill=(30, 41, 59), outline=(124, 58, 237), width=8)
    d.rectangle([cx - 135, cy - 220, cx + 135, cy + 220], fill=(237, 233, 254))
    draw_circle(d, cx, cy, 74, outline=(244, 63, 94), width=6)
    draw_circle(d, cx, cy, 46, fill=(124, 58, 237))
    draw_circle(d, cx, cy, 18, fill=(255, 255, 255))
    d.rectangle([72, 340, 190, 348], fill=(124, 58, 237))
    return img


GENERATORS = {
    "computer-networking.webp": gen_computer_networking,
    "advanced-networking.webp": gen_advanced_networking,
    "linux-fundamentals.webp": gen_linux_fundamentals,
    "kali-linux.webp": gen_kali_linux,
    "linux-administration.webp": gen_linux_administration,
    "ethical-hacking.webp": gen_ethical_hacking,
    "penetration-testing.webp": gen_penetration_testing,
    "web-security.webp": gen_web_security,
    "owasp-top10.webp": gen_owasp_top10,
    "python-cybersecurity.webp": gen_python_cybersecurity,
    "bash-scripting.webp": gen_bash_scripting,
    "osint-guide.webp": gen_osint_guide,
    "wireshark.webp": gen_wireshark,
    "nmap.webp": gen_nmap,
    "digital-forensics.webp": gen_digital_forensics,
    "cryptography.webp": gen_cryptography,
    "malware-analysis.webp": gen_malware_analysis,
    "windows-security.webp": gen_windows_security,
    "soc-analyst.webp": gen_soc_analyst,
    "incident-response.webp": gen_incident_response,
    "cloud-security.webp": gen_cloud_security,
    "api-security.webp": gen_api_security,
    "wireless-security.webp": gen_wireless_security,
    "mobile-security.webp": gen_mobile_security,
}


def main():
    for filename, fn in GENERATORS.items():
        img = fn()
        img.save(os.path.join(OUTPUT_DIR, filename), "WEBP", quality=92, method=6)
    print(f"Regenerated {len(GENERATORS)} clean editorial covers.")


if __name__ == "__main__":
    main()
