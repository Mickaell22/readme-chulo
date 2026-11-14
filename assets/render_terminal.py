#!/usr/bin/env python3
"""Hero de terminal para READMEs de tools sin UI (CLI / MCP / lib).
Genera un PNG estilo screenshot de terminal con salida REAL del proyecto.
Rellenar el bloque CONFIG con datos reales (no inventar) y correr:
    python3 render_terminal.py
Requiere Pillow (PIL). Sin deps de red."""
from PIL import Image, ImageDraw, ImageFont

# ------- CONFIG (rellenar con datos REALES) -------
OUT = "docs/screenshots/hero.png"          # ruta de salida (relativa al repo)
PROMPT = [("$ ", "cyan"), ("mi-tool ", "white"), ("▸ ", "cyan"), ("comando", "green")]
BOX_TITLE = " Nombre del Proyecto "
BOX_LINE1 = [("N cosas reales", "fg"), ("   ·   ", "magenta"), ("subtitulo real", "fg")]
BOX_LINE2 = "linea tecnica gris (stack, motor, etc.)"
BOX_LINE3 = "continuacion opcional"
COL_HEADERS = ("Columna A", "Columna B")   # header de la tabla
ROWS = [                                    # (col_a, col_b) — datos REALES
    # ("item", "valor"),
]
SHOWN = 13
REST_LABEL = "… y {n} más"                  # {n} = TOTAL - filas mostradas
TOTAL = 0                                   # total real (para el "y N mas")
FOOTER = "sub_comando_a · sub_comando_b · …"
# --------------------------------------------------

C = {"bg": "#0d0d0f", "fg": "#e6edf3", "dim": "#6e7681", "cyan": "#39d3e8",
     "green": "#3fdd78", "magenta": "#e05fd8", "white": "#f0f6fc"}
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
PAD, LH, FS, W = 70, 46, 30, 1640

def fnt(sz, bold=False):
    return ImageFont.truetype(MONO_B if bold else MONO, sz)

n_lines = 1 + 1 + 5 + 1 + 3 + SHOWN + 1 + 1 + 2
H = PAD * 2 + 120 + LH * n_lines
img = Image.new("RGB", (W, H), C["bg"]); d = ImageDraw.Draw(img)
base, bold = fnt(FS), fnt(FS, True)

for i, c in enumerate(("#ff5f56", "#ffbd2e", "#27c93f")):
    d.ellipse([60 + i*46, 55, 90 + i*46, 85], fill=c)

def line(segs, yy, f, x0=PAD):
    x = x0
    for text, col in segs:
        d.text((x, yy), text, font=f, fill=C.get(col, col)); x += d.textlength(text, font=f)

y = 150
line(PROMPT, y, bold); y += LH*2

bx0, bx1, by0 = PAD, W-PAD, y
tw = d.textlength(BOX_TITLE, font=bold); tcx = (bx0+bx1)/2 - tw/2
d.line([bx0+16, by0, tcx-12, by0], fill=C["magenta"], width=2)
d.line([tcx+tw+12, by0, bx1-16, by0], fill=C["magenta"], width=2)
d.text((tcx, by0-FS//2-2), BOX_TITLE, font=bold, fill=C["magenta"])
iy, ip = by0+28, PAD+22
line(BOX_LINE1, iy, base, ip)
line([(BOX_LINE2, "dim")], iy+LH, base, ip)
line([(BOX_LINE3, "dim")], iy+LH*2, base, ip)
by1 = iy + LH*3 + 8
for seg in ([bx0, by0, bx0, by1], [bx1, by0, bx1, by1], [bx0, by1, bx1, by1]):
    d.line(seg, fill=C["magenta"], width=2)
y = by1 + LH*2

COL2 = W - PAD - 360
line([(COL_HEADERS[0], "cyan")], y, bold)
d.text((COL2, y), COL_HEADERS[1], font=bold, fill=C["cyan"]); y += LH-8
d.line([PAD, y, COL2+330, y], fill="#30363d", width=3); y += 14
for a, b in ROWS[:SHOWN]:
    d.text((PAD, y), a, font=base, fill=C["fg"]); d.text((COL2, y), b, font=base, fill=C["green"]); y += LH
rest = TOTAL - min(SHOWN, len(ROWS))
if rest > 0:
    d.text((PAD, y), REST_LABEL.format(n=rest), font=base, fill=C["dim"]); y += LH
y += LH
line([("  " + FOOTER, "dim")], y, base)

img.save(OUT, "PNG"); print("OK ->", OUT)
