# Genera el titulo animado estilo CASCADE (letras que caen con rebote + punto
# "online" que late + subtitulo rotativo). Escribe docs/screenshots/title-{dark,light}.svg
# en el cwd; usarlos con <picture> (prefers-color-scheme). Uso: python3 title_cascade.py
# Adaptar: NAME, PHRASES (frases REALES del proyecto) y THEMES (acento del repo).
from xml.sax.saxutils import escape

NAME = "Mickaell Morán"
PHRASES = ["Desarrollador Fullstack", "Python · React · Flutter", "Guayaquil, Ecuador"]
W, H, FS = 820, 170, 64
CW = FS * 0.6                     # ancho de caracter monospace
STAGGER, DUR = 0.07, 0.65         # segundos entre letras / duracion de cada caida
FONT = "'DejaVu Sans Mono','JetBrains Mono','Consolas',monospace"
THEMES = {
    "dark":  {"name": "#fafafa", "sub": "#a1a1aa", "dot": "#22c55e"},
    "light": {"name": "#09090b", "sub": "#52525b", "dot": "#16a34a"},
}

def build(c):
    start = (W - len(NAME) * CW) / 2 - CW / 2   # deja sitio al punto
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none" role="img" aria-label="{escape(NAME)}">']
    for i, ch in enumerate(NAME):
        if ch == " ":
            continue
        x = start + (i + 0.5) * CW
        b = f"{i * STAGGER:.2f}s"
        out.append(
            f'  <text x="{x:.1f}" y="88" text-anchor="middle" font-family="{FONT}" font-size="{FS}" font-weight="bold" fill="{c["name"]}" opacity="0">{escape(ch)}'
            f'<animate attributeName="opacity" values="0;1" begin="{b}" dur="{DUR * 0.6:.2f}s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" values="0 -46;0 6;0 -2;0 0" keyTimes="0;0.55;0.8;1" begin="{b}" dur="{DUR}s" fill="freeze" calcMode="spline" keySplines="0.3 0 0.7 1;0.3 0 0.7 1;0.3 0 0.7 1"/></text>')
    end = len(NAME) * STAGGER + DUR       # cuando aterriza la ultima letra
    dx = start + len(NAME) * CW + 22
    out.append(f'  <circle cx="{dx:.1f}" cy="66" r="0" fill="{c["dot"]}" opacity="0.35">'
               f'<animate attributeName="r" values="7;16;7" begin="{end:.2f}s" dur="2s" repeatCount="indefinite"/>'
               f'<animate attributeName="opacity" values="0.45;0;0.45" begin="{end:.2f}s" dur="2s" repeatCount="indefinite"/></circle>')
    out.append(f'  <circle cx="{dx:.1f}" cy="66" r="0" fill="{c["dot"]}">'
               f'<animate attributeName="r" values="0;9;7" keyTimes="0;0.6;1" begin="{end:.2f}s" dur="0.4s" fill="freeze"/></circle>')
    n, cyc = len(PHRASES), 3.0           # 3s por frase
    total = n * cyc
    for k, p in enumerate(PHRASES):
        a, f = k / n, 0.4 / total        # inicio de la ventana y fade de 0.4s
        kt = [0, a, a + f, a + 1 / n - f, a + 1 / n, 1]
        kt = [min(1, round(t, 4)) for t in kt]
        vals = "0;0;1;1;0;0"
        if k == n - 1:                     # la ultima ventana termina justo en 1
            kt, vals = kt[:-1], "0;0;1;1;0"
        out.append(f'  <text x="{W / 2:.0f}" y="140" text-anchor="middle" font-family="{FONT}" font-size="22" fill="{c["sub"]}" opacity="0">{escape(p)}'
                   f'<animate attributeName="opacity" values="{vals}" keyTimes="{";".join(map(str, kt))}" begin="{end:.2f}s" dur="{total:.0f}s" repeatCount="indefinite"/></text>')
    out.append("</svg>\n")
    return "\n".join(out)

for theme, colors in THEMES.items():
    open(f"docs/screenshots/title-{theme}.svg", "w").write(build(colors))

# self-check: letras dentro del lienzo y keyTimes validos para SMIL
import re
for theme in THEMES:
    s = open(f"docs/screenshots/title-{theme}.svg").read()
    xs = [float(x) for x in re.findall(r'<text x="([\d.]+)" y="88"', s)]
    assert min(xs) - CW / 2 >= 0 and max(xs) + CW / 2 + 22 + 16 <= W, xs
    for kt in re.findall(r'keyTimes="([^"]+)"', s):
        t = [float(v) for v in kt.split(";")]
        assert t[0] == 0 and t[-1] == 1 and t == sorted(t), kt
print("ok")
