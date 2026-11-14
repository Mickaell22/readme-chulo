"""Vista previa fiel de un README: lo renderiza con el motor de GitHub y saca captura.

Uso (desde la raiz del repo):
    python3 -I ~/.claude/skills/readme-chulo/assets/preview_shot.py README.md /tmp/preview.png [--open-details]

- Renderiza con `gh api markdown` en mode=markdown (NO gfm: gfm convierte cada
  salto de linea en <br> y apila los badges en columna, cosa que en el README
  real no pasa).
- Reescribe las imagenes relativas a file:// para ver los assets locales sin pushear.
- Captura full-page con Playwright, tema oscuro. Navegador: $CHROMIUM_PATH, o chromium del PATH.
- Limitacion conocida: con el CSS de github-markdown-dark las tablas pueden
  salir con texto apagado; en GitHub se ven normales.
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import os
import shutil
from playwright.sync_api import sync_playwright

CSS = "https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-dark.min.css"


def main():
    readme, out = Path(sys.argv[1]).resolve(), sys.argv[2]
    body = subprocess.run(["gh", "api", "markdown", "--input", "-"], check=True, capture_output=True, text=True,
                          input=json.dumps({"text": readme.read_text(), "mode": "markdown"})).stdout
    base = readme.parent
    body = re.sub(r'src="(?:\./)?(?!https?:|file:|data:)([^"]+)"', lambda m: f'src="file://{base / m.group(1)}"', body)
    html = (f'<html><head><meta charset="utf-8"><link rel="stylesheet" href="{CSS}"><style>body{{background:#0d1117;'
            f'margin:0}}.markdown-body{{max-width:1012px;margin:0 auto;padding:32px}}</style></head>'
            f'<body><article class="markdown-body">{body}</article></body></html>')
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or shutil.which("chromium") or "/usr/bin/chromium", args=["--no-sandbox", "--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1100, "height": 900})
        pg.goto(f"file://{f.name}")
        pg.wait_for_timeout(2500)  # deja correr las animaciones SMIL un poco
        if "--open-details" in sys.argv:
            for d in pg.query_selector_all("details"):
                d.evaluate("e => e.open = true")
        pg.screenshot(path=out, full_page=True)
        b.close()
    print(out)


if __name__ == "__main__":
    main()
