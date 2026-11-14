# Titulo split-flap (tablero de aeropuerto): cada ficha baraja letras y se asienta en la final.
# Primer frame = palabra final (legible donde no hay animacion).
import random, sys
random.seed(7)
WORD, OUT = sys.argv[1], sys.argv[2]
W, H, GAP, TOP = 74, 96, 10, 14
DUR = 7.0                       # ciclo completo
FLIPS = 4                        # letras falsas por ficha
STEP = 0.09                      # segundos por letra falsa
n = len(WORD); total_w = n*W + (n-1)*GAP; width = total_w + 40
alpha = "ABCDEFGHJKLMNPRSTUVWXYZ0123456789"
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{H+TOP*2}" viewBox="0 0 {width} {H+TOP*2}" role="img" aria-label="{WORD}">',
       '  <g font-family="\'DejaVu Sans Mono\',\'JetBrains Mono\',Consolas,monospace" font-size="60" font-weight="bold" text-anchor="middle">']
for i, ch in enumerate(WORD):
    x = 20 + i*(W+GAP); cx = x + W/2; ty = TOP + H/2 + 21
    start = 0.6 + i*0.12                       # cascada izquierda -> derecha
    end = start + FLIPS*STEP
    k = lambda t: f"{t/DUR:.4f}"
    color = "#ffc940" if i < 5 else "#3fdd78"  # AJUSTAR: en ApplyJob, "Apply" ambar y "Job" verde
    out.append(f'    <rect x="{x}" y="{TOP}" width="{W}" height="{H}" rx="9" fill="#161b22" stroke="#30363d" stroke-width="2"/>')
    # letra final: visible al inicio, se apaga mientras baraja, vuelve y se queda
    out.append(f'    <text x="{cx}" y="{ty}" fill="{color}">{ch}<animate attributeName="opacity" calcMode="discrete" '
               f'values="1;0;1" keyTimes="0;{k(start)};{k(end)}" dur="{DUR}s" repeatCount="indefinite"/></text>')
    for f in range(FLIPS):
        a, b = start + f*STEP, start + (f+1)*STEP
        c = random.choice(alpha.replace(ch.upper(), ""))
        out.append(f'    <text x="{cx}" y="{ty}" fill="#8b949e" opacity="0">{c}<animate attributeName="opacity" calcMode="discrete" '
                   f'values="0;1;0" keyTimes="0;{k(a)};{k(b)}" dur="{DUR}s" repeatCount="indefinite"/></text>')
    # bisagra de la ficha, encima de las letras
    out.append(f'    <rect x="{x}" y="{TOP+H/2-1.5}" width="{W}" height="3" fill="#0d1117"/>')
out += ['  </g>', '</svg>']
open(OUT, "w").write("\n".join(out) + "\n")
