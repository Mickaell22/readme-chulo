---
name: readme-chulo
description: Crea o rediseña un README.md de proyecto con un "hero" visual, atractivo y profesional al estilo de los repos top de GitHub (screenshot arriba, div centrado, filas de badges de shields.io, links de comunidad y navegación interna). Usar cuando el usuario pida hacer, mejorar, "hacer chulo/bonito/vistoso", rediseñar o dar formato a un README, un readme de GitHub, la portada de un repo, o un landing/hero de proyecto en Markdown. Tambien para el README de PERFIL de GitHub (repo usuario/usuario). Trigger words: readme, README.md, portada del repo, perfil de GitHub, hero, badges, shields.io.
---

# README chulo

Genera el encabezado ("hero") y la estructura de un `README.md` con la maqueta
que usan los repos populares de GitHub: imagen del producto arriba, todo centrado,
filas de badges que cuentan una historia (prestigio -> features -> comunidad ->
distribucion) y navegacion interna por anclas.

## Cuando usarla

- "hazme un README chulo / bonito / vistoso para X"
- "mejora/rediseña la portada de este repo"
- "ponle badges y un hero al README"
- "dale formato profesional a mi README.md"

Si el proyecto ya tiene contenido tecnico bueno pero se ve plano, esta skill se
encarga SOLO de la maqueta visual y la distribucion; no reescribe la doc tecnica
salvo que lo pidan.

## Regla de honestidad (no negociable)

El objetivo es que se vea profesional, NO inflar. Prohibido inventar cifras
(stars, tests, usuarios, benchmarks, "% de ahorro"). Cada numero o claim del
hero debe salir de un dato real del proyecto o del usuario. Un README vistoso
con datos falsos es peor que uno feo honesto. Si falta un dato, se deja un
placeholder `<!-- TODO: dato real -->` en vez de rellenar con humo.

## Anatomia del hero (el patron)

Todo el encabezado va dentro de UN solo `<div align="center"> ... </div>`.
En GitHub el Markdown se alinea a la izquierda; centrar exige HTML. Dentro del
div, el espaciado de parrafos se pierde, asi que se usan `<br/>` manuales.

Orden de arriba hacia abajo:

1. **Screenshot / logo del producto** ANTES del titulo. Ruta relativa versionada
   en el repo (`./docs/screenshots/...`), no hotlink externo. `width` fijo.
   Para tema claro/oscuro usar `<picture>` con `<source media="(prefers-color-scheme: dark)">`.
   Si el proyecto es una herramienta SIN UI (CLI, MCP server, libreria), la
   imagen NO tiene que ser un dashboard: vale mas un **terminal en accion** (ver
   "Hero de terminal" abajo).
2. **Titulo animado** (default de esta skill) o `#` de texto plano. El texto
   plano se ve simple; preferir un **SVG animado autocontenido** (ver "Titulo
   animado" abajo). Debajo, un `###` con la promesa en UNA frase.
3. **Sub-claims** cortos en negrita separados por `<br/>`.
4. (Opcional) **Call-to-star** en un `<h3>`.
5. **Badges de prestigio**: stars, star-history, Trendshift, etc.
6. **Badges de features** (`style=for-the-badge`, colores hex de marca), cada uno
   enlazando a su ancla `#-seccion`.
7. **Badges de comunidad**: Discord, Telegram, Website... con `logo=` de la marca.
8. **Badges de distribucion**: npm/pypi version, Docker pulls, License, downloads.
   Dan sensacion de "producto vivo y usado".
9. **Una o dos filas de navegacion interna** con links a anclas, separados por ` • `.

Se cierra el `</div>` y de ahi hacia abajo va la doc normal, alineada a la
izquierda: contraste entre hero vistoso arriba y doc sobria abajo.

## Titulo animado (default) — CON VARIEDAD entre repos

El nombre en texto plano se ve simple. Por defecto, usar un **SVG animado
commiteado al repo** (`docs/screenshots/title.svg`), NO un servicio externo tipo
readme-typing-svg (evita hotlink y dependencia de terceros). GitHub renderiza
animaciones SMIL cuando el SVG se embebe como `<img>`.

**Regla de variedad (no negociable): no repitas el mismo estilo de animacion
en repos distintos del mismo usuario.** Si todos los READMEs llevan el mismo
shimmer deja de ser un detalle y parece plantilla. Antes de elegir:
1. Pregunta al usuario (o revisa sus otros READMEs si estan en disco) que
   estilo ya se uso donde. Ej.: si `mcp-context-server` ya usa shimmer, el
   siguiente repo usa otro.
2. Elige el estilo que pegue con la personalidad del proyecto, no el primero.

Estilos disponibles (uno por archivo en `assets/`):

| Estilo | Archivo | Se ve como | Pega con |
|---|---|---|---|
| Shimmer | `title.svg` | gradiente que barre el wordmark + flotado sutil | default generico, frontends, portfolios |
| Typewriter | `title-typewriter.svg` | el nombre se escribe caracter a caracter, cursor de bloque que sigue el tipeo y parpadea | CLIs, MCP servers, dashboards, tools de terminal |
| Glow | `title-glow.svg` | neon que respira detras del texto nitido | dark themes, productos premium, juegos, media |
| Underline | `title-underline.svg` | fade-in + subrayado que se dibuja + punto de acento que aterriza | librerias, backends, docs, proyectos sobrios |
| Cascade | `title_cascade.py` (generador, salida clara+oscura) | letras que caen una a una con rebote, punto "online" que late, subtitulo rotativo | portfolios, perfiles personales, landings |
| Spin | `title-spin.svg` | icono/disco que gira (animateTransform) + wordmark revelado con clipPath | apps de media/musica, productos con logo circular |
| Glitch | `title-glitch.svg` | wordmark quieto que cada ~3s falla: copias rosa/celeste desfasadas a saltos + franjas cortadas (clipPath) | tools de terminal con humor, seguridad, cosas random |
| Marquee | `banner_marquee.py` (generador, banner ancho 1000x300) | destello que recorre el borde (stroke-dashoffset), frases de rol que rotan con fade+slide, cinta de tecnologias en bucle | perfiles de GitHub, landings de persona/equipo |
| Split-flap | `title_flap.py PALABRA salida.svg` (generador) | fichas de tablero de aeropuerto que barajan letras y se asientan en cascada | agregadores, pipelines, tableros, cosas con "listas" |
| Draw | `title-draw.svg` | el trazo (stroke-dashoffset) dibuja el nombre y despues se rellena | herramientas de diseño, colecciones, cosas "hechas a mano" |

**Registro de lo usado: `README.md` de esta carpeta** (seccion Catalogo). Esta carpeta es el repo
publico `github.com/Mickaell22/readme-chulo`. Leer el catalogo ANTES de elegir estilo y colores.
Al terminar un README nuevo: copiar su titulo a `galeria/<repo>.svg`, agregar su celda a la Galeria,
su fila al Catalogo y marcar el estilo en "Estilos de titulo"; luego commit + push de esta carpeta
(con autorizacion del usuario y sin ninguna linea de atribucion).

Si todos ya se usaron en otros repos, crea una variante nueva combinando
tecnicas SMIL (clip-path animado, stroke-dashoffset, blur, steps discrete)
antes que repetir, y considera guardarla aqui como quinto asset.

- Tuneo: cada plantilla trae en su comentario de cabecera las instrucciones
  exactas de adaptacion. Lo comun: wordmark en fuente monospace; al cambiar el
  texto ajustar las coords `x` para centrar (mono ≈ 0.6em por char). El
  typewriter ademas requiere regenerar las listas `values`/`keyTimes`.
- Colores siempre coherentes con los badges/acento del proyecto.
- En el README: `<img src="./docs/screenshots/title.svg" alt="NOMBRE" width="560"/>`
  en lugar del `# Titulo`. Poner `alt` real (SEO/accesibilidad, ya no hay `<h1>`).
- **Particulas con `animateMotion`**: un `begin="0.8s"` deja la particula dibujada en (0,0) hasta
  que arranca (punto suelto en la esquina del primer frame y de las capturas). Usar retrasos
  negativos (`begin="-0.8s"`): la animacion ya esta en curso desde el frame 0.
- **Primer frame legible**: donde no hay animacion (rsvg, npm, lectores) se ve el
  estado inicial. Lo que entra con fade (frases rotativas, etc.) debe tener el
  PRIMER elemento con opacity 1 por defecto, si no el banner sale vacio.
- **Caveat honesto que hay que decirle al usuario**: GitHub web anima; sitios que
  rasterizan el README (npm, algunos readers) muestran el primer frame estatico
  — se lee igual, solo no se mueve.

## Elegir la imagen del hero SEGUN el proyecto (no hay regla unica)

La imagen se decide por lo que el proyecto tiene para mostrar. NO forzar terminal
siempre ni dashboard siempre. Preguntar/mirar que es el proyecto y elegir:

- **Frontend / app con UI**: screenshot REAL del dashboard/pantalla principal.
  Es lo que el usuario ve; la captura vende sola. (`docs/screenshots/*.png`)
- **Backend / API / servicio**: es dificil de mostrar visualmente. Elegir lo que
  mejor represente SU valor: salida de terminal real, un request/response de
  ejemplo, una tabla de endpoints, o un diagrama de arquitectura (mermaid).
- **CLI / MCP server / libreria sin UI**: terminal en accion con salida REAL
  (ver "Hero de terminal" abajo).
- **Monorepo front+back**: normalmente gana el screenshot del front (lo visible);
  el back se luce en el cuerpo con diagrama/tabla.

Ante la duda, preguntar al usuario que quiere mostrar. La imagen debe representar
lo que el proyecto ES, no rellenar por rellenar.

## Hero de terminal (para CLI / MCP / libs / backends sin nada visual)

Cuando el proyecto no tiene front (o es un back dificil de representar), la mejor
imagen es el propio comando corriendo con salida REAL, estilo screenshot de
terminal (traffic lights, prompt, output). Es mas honesto que inventar un dashboard.

- Generador en `assets/render_terminal.py` (PIL, sin deps de red). Rellenar el
  bloque `DATA` con salida REAL (ej. de la propia tool) — nunca inventar conteos
  ni filas.
- Estetica: fondo oscuro, 3 traffic lights, prompt `$ tool ▸ comando`, caja con
  borde de color y titulo en el borde, tabla con headers en cyan y valores en
  verde, footer con nombres de sub-comandos.
- Respetar acentos del español (semántica, Último, más): `DejaVuSansMono` tiene
  los glifos; los emoji NO (usan tofu) — evitarlos en el PNG o dibujarlos aparte.

## README de PERFIL de GitHub (repo `usuario/usuario`)

No es un README de proyecto: es una portada personal. Investigacion (2026,
awesome-github-profile-readme, readmedesign, devbio) + lo que el usuario
rechazo en la practica:

**Lo que el usuario rechazo (no repetir):**
- Hero "terminal whoami" (PNG de consola con `$ whoami`): cansa, se ve plantilla.
- "Arriba se ve bien y abajo es solo texto": proyectos y experiencia como
  parrafos largos. El cuerpo tambien tiene que ser visual, no solo el hero.

**Que funciona:**
- Texto total 100-250 palabras visibles. Lo largo va dentro de
  `<details><summary><b>...</b></summary>` (se pliega por defecto).
- Intro de 1 linea + 3 bullets cortos (Ahora / Construyendo / Me importa).
  Nada de "apasionado por la tecnologia".
- **Proyectos como tarjetas en grilla**: `<table>` de 2 columnas, cada celda con
  una portada PNG generada (`assets/render_covers.py`) envuelta en `<a>` al repo
  y debajo una linea de links (`app · backend · panel`). 4-6 destacados; el resto
  en una tabla `Proyecto | Qué hace | Stack` dentro de `<details>`.
  - Portada: tag de estado (EN PRODUCCIÓN, CLIENTE REAL...), nombre, una frase
    con dato real, chips de stack; a la derecha la CAPTURA REAL del proyecto
    (marco de navegador o de telefono) o, si no hay, tiles con iconos del stack.
  - Antes de destacar un proyecto, preguntar si esta terminado: no destacar lo
    que el usuario aun esta construyendo (paso con Surco).
- **Stack como grilla de iconos** (`assets/render_stack.py`): un SVG
  autocontenido con los paths de simple-icons embebidos, agrupado por area.
  Reemplaza los muros de 40 badges. Iconos: `npm pack simple-icons` en un dir
  vacio y copiar solo los `.svg` usados (CC0) a `docs/build/icons/`. Marcas que
  simple-icons retiro (C#, Java, SQL Server, Playwright, OpenAI) van como
  monograma de texto. Colores de marca oscuros se aclaran para fondo oscuro.
- **Experiencia como tabla** `Periodo | Rol | Dónde` + detalle en `<details>`.
- Formacion/certificados como badges `flat-square` en una sola fila.
- Todos los assets visuales llevan su propio fondo oscuro con esquinas
  redondeadas: asi se ven igual en tema claro y oscuro sin `<picture>`.
- Generadores versionados en `docs/build/`, salida en `docs/assets/`.
- Datos: sacarlos del CV / bitacora del usuario y de las descripciones de sus
  repos (`gh repo list USER --json name,description,visibility`). Si dos fuentes
  se contradicen (ej. "7 fuentes" vs "13 fuentes"), gana la mas reciente y se
  avisa al usuario.
- Experiencia en curso en una empresa: nombrarla esta bien, pero NADA interno
  (tablas, SP, clientes, vulnerabilidades encontradas): el perfil es publico.

**Que evitar:**
- Widgets dinamicos de terceros (github-readme-stats, streak, trofeos, snake,
  contadores de visitas): se caen o quedan rate-limited y una imagen rota es
  peor que ninguna; ademas en 2026 se leen como plantilla. Como mucho UNO.
- Emojis en titulos (rompen anclas) y titulos con signos (`&`, `:`).
- Un mismo CTA repetido tres veces; links a cosas muertas.

## Verificar antes de entregar (obligatorio)

Nunca entregar un README sin haberlo visto renderizado:

    python3 -I ~/.claude/skills/readme-chulo/assets/preview_shot.py README.md /tmp/preview.png --open-details

Usa el renderer real de GitHub (`gh api markdown`, mode=markdown) y saca captura
full-page con Playwright, con los assets locales. Revisar la captura por partes
(recortar con `convert -crop`) buscando: textos ilegibles a tamano de celda,
imagenes cortadas, badges apilados, secciones que sean pared de texto.
Para ver animaciones SVG en varios instantes, abrir el SVG en una pagina y
capturar a distintos tiempos con Playwright (`page.wait_for_timeout`).

No abrir el resultado en VS Code u otras apps GUI desde la sesion de Claude
(corre como otro usuario/sin sesion grafica y la ventana se queda colgada,
bloqueando la instancia del usuario). Mostrar la captura o decirle al usuario
el comando para abrirlo el.

## shields.io (cheatsheet)

- Estatico: `https://img.shields.io/badge/ETIQUETA-MENSAJE-HEXCOLOR?style=for-the-badge`
  - Espacio = `_` o `%20`; guion literal = `--`; `%2B` = `+`, `%25` = `%`.
- Dinamicos utiles:
  - Stars: `https://img.shields.io/github/stars/USER/REPO?style=social`
  - Downloads GH: `https://img.shields.io/github/downloads/USER/REPO/total`
  - npm version: `https://img.shields.io/npm/v/PAQUETE`
  - npm mes: `https://img.shields.io/npm/dm/PAQUETE`
  - Docker pulls: `https://img.shields.io/docker/pulls/USER/IMAGEN`
  - PyPI: `https://img.shields.io/pypi/v/PAQUETE`
  - Licencia: `https://img.shields.io/badge/License-MIT-yellow.svg`
- Con logo de marca: agregar `&logo=discord&logoColor=white`.
- Badge que ademas navega:
  `[![Alt](URL_DEL_BADGE)](#ancla-o-link)`. Las anclas de GitHub son el titulo
  en minusculas, espacios -> `-`, sin emojis ni signos.

## Flujo

1. Reunir los datos REALES: nombre, tagline de una frase, lenguaje/stack, si hay
   npm/pypi/docker, links de comunidad, si existe screenshot (o pedir que lo
   agreguen en `docs/screenshots/`). No inventar; usar placeholders si falta.
2. **Imagen del hero**: si hay UI, screenshot real; si es CLI/MCP/lib sin UI,
   generar un hero de terminal con salida real (`assets/render_terminal.py`).
3. **Titulo animado**: elegir UN estilo de `assets/title*.svg` que no se haya
   usado en otros repos del usuario (ver "Regla de variedad"), copiarlo como
   `docs/screenshots/title.svg`, cambiar texto/colores, tunear coords, y
   embeberlo con `<img ... width="560"/>` en vez del `# Titulo`.
4. Copiar el esqueleto de `assets/template.md` y rellenarlo con esos datos.
5. Elegir 3-6 badges de features reales; asignar colores hex coherentes.
6. Ajustar las anclas de navegacion a las secciones que el README vaya a tener.
7. Si el repo ya tiene README, conservar el cuerpo tecnico y reemplazar/insertar
   solo el bloque hero.

8. Renderizar y revisar con `assets/preview_shot.py` antes de entregar.

Assets: `assets/template.md` (esqueleto), `assets/title*.svg` (nombres animados),
`assets/render_terminal.py` (hero de terminal para tools sin UI),
`assets/banner_marquee.py` (banner de perfil), `assets/render_covers.py`
(portadas de proyecto), `assets/render_stack.py` (grilla de iconos del stack),
`assets/preview_shot.py` (vista previa fiel con el renderer de GitHub).
Los tres generadores de perfil son la version real usada en Mickaell22: copiarlos
al repo destino y cambiar sus listas de datos (NAME/ROLES/TECH, COVERS, ROWS).
