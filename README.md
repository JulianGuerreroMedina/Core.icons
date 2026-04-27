# Core.icons

Core.icons es una biblioteca estatica de iconos SVG/PNG para proyectos web.
Expone una hoja de estilos CSS con clases utilitarias, un catalogo visual HTML,
un manifiesto JSON del inventario y un script de validacion para mantener
sincronizadas las referencias entre CSS, assets y metadata.

Esta pensado para desarrolladores frontend/backend, administradores de sistemas
y mantenedores que necesiten publicar y reutilizar un set comun de iconos en
aplicaciones web internas o externas.

## Tabla de contenido

- [Descripcion general](#descripcion-general)
- [Caracteristicas principales](#caracteristicas-principales)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos previos](#requisitos-previos)
- [Instalacion](#instalacion)
- [Uso](#uso)
- [Catalogo visual](#catalogo-visual)
- [Manifest del catalogo](#manifest-del-catalogo)
- [Validacion](#validacion)
- [Ejecucion con Docker](#ejecucion-con-docker)
- [Despliegue](#despliegue)
- [Configuracion](#configuracion)
- [Mantenimiento](#mantenimiento)
- [Seguridad y datos sensibles](#seguridad-y-datos-sensibles)
- [Pendiente por documentar](#pendiente-por-documentar)
- [Licencia](#licencia)

## Descripcion general

El proyecto centraliza iconos reutilizables y los publica como recursos
estaticos. La integracion principal se realiza incluyendo `style_icons.css` en
una pagina web y usando las clases CSS disponibles sobre elementos HTML como
`span`, `i` o componentes equivalentes.

Flujo general:

1. Los archivos de iconos viven en `icons/`.
2. `style_icons.css` define clases CSS que asignan cada icono como
   `background-image`.
3. `manifest.json` registra el catalogo de iconos con clase, asset, categoria y
   formato.
4. `index.html` muestra una galeria visual de las clases disponibles.
5. `scripts/validate_icons.py` valida que las referencias del CSS y del
   manifest apunten a archivos existentes y que no haya clases CSS duplicadas.

No se detecta backend de aplicacion, base de datos, autenticacion, API dinamica
ni proceso de compilacion. El repositorio funciona como paquete/hosting
estatico de assets.

## Caracteristicas principales

- Biblioteca de iconos reutilizable mediante clases CSS.
- Soporte para assets SVG y PNG.
- Galeria HTML responsive para inspeccionar visualmente el catalogo.
- Agrupacion visual de iconos en la galeria mediante JavaScript del lado del
  cliente.
- Manifest JSON para consumir o auditar el inventario desde herramientas
  externas.
- Script de validacion de integridad entre `style_icons.css`, `manifest.json` e
  `icons/`.
- Entorno local opcional con Apache `httpd:alpine` mediante Docker Compose.
- Licencia MIT.

## Tecnologias utilizadas

| Tecnologia | Uso dentro del proyecto |
|---|---|
| HTML | Galeria visual del catalogo en `index.html` |
| CSS | Definicion de clases utilitarias en `style_icons.css` |
| JavaScript | Agrupacion dinamica de iconos dentro de la galeria |
| JSON | Catalogo estructurado en `manifest.json` |
| Python 3 | Script de validacion `scripts/validate_icons.py` |
| SVG / PNG | Formatos de los assets en `icons/` |
| Docker Compose | Ejecucion local opcional del catalogo |
| Apache httpd | Servidor web usado por el compose local |
| Google Fonts | Fuentes usadas por `index.html` para la galeria visual |

## Estructura del proyecto

```text
core.icons/
├── icons/                    # Assets SVG/PNG
├── scripts/
│   └── validate_icons.py     # Validador de integridad del catalogo
├── docker/
│   └── docker-compose.yml    # Servidor local Apache
├── index.html                # Galeria visual de iconos
├── manifest.json             # Catalogo estructurado
├── style_icons.css           # Clases CSS reutilizables
├── LICENSE                   # Licencia MIT
└── README.md                 # Documentacion del proyecto
```

Archivos principales:

| Ruta | Descripcion |
|---|---|
| `style_icons.css` | Define las clases CSS de iconos y sus rutas `url(...)` hacia `icons/`. |
| `icons/` | Contiene los archivos SVG/PNG publicados por la biblioteca. |
| `manifest.json` | Lista las clases disponibles y su asset asociado. |
| `index.html` | Pagina estatica para revisar el catalogo en navegador. |
| `scripts/validate_icons.py` | Comprueba referencias faltantes y clases duplicadas. |
| `docker/docker-compose.yml` | Sirve el repositorio completo con Apache en el puerto `8014`. |

## Requisitos previos

Para usar la biblioteca como archivos estaticos:

- Navegador web moderno.
- Servidor HTTP estatico si se publica en red.

Para validar el catalogo:

- Python 3.

Para ejecutar el servidor local incluido:

- Docker.
- Docker Compose v2, disponible normalmente como `docker compose`.

No se detectan dependencias de Composer, npm, pip, framework backend ni base de
datos.

## Instalacion

Clona el repositorio y entra al directorio del proyecto:

```bash
git clone URL_DEL_REPOSITORIO
cd core.icons
```

Valida el estado del catalogo:

```bash
python3 scripts/validate_icons.py
```

Salida esperada en el estado actual del proyecto:

```text
OK: 89 CSS refs, 89 unique classes, 89 manifest entries
```

Si solo necesitas consumir la biblioteca, publica o copia al menos estos
elementos respetando la misma estructura relativa:

```text
style_icons.css
icons/
```

`index.html`, `manifest.json` y `scripts/validate_icons.py` son utiles para
revision, automatizacion y mantenimiento, pero no son obligatorios para que las
clases CSS rendericen los iconos.

## Uso

Incluye la hoja de estilos desde el host donde publiques el repositorio:

```html
<link rel="stylesheet" href="https://TU-DOMINIO/core.icons/style_icons.css">
<span class="btn-save" aria-hidden="true"></span>
```

Uso con ruta local o relativa:

```html
<link rel="stylesheet" href="/style_icons.css">
<span class="btn-file-download" aria-hidden="true"></span>
```

Las clases usan `background-image`, por lo que los assets deben conservar la ruta
relativa esperada por el CSS:

```css
.btn-save {
  background: url(icons/btn-save.svg) no-repeat center center;
}
```

Si mueves `style_icons.css` a otra carpeta, tambien debes ajustar las rutas
`url(icons/...)` o publicar `icons/` en una ubicacion relativa equivalente.

Ejemplos de clases disponibles:

```html
<span class="btn-file" aria-hidden="true"></span>
<span class="btn-folder" aria-hidden="true"></span>
<span class="btn-user" aria-hidden="true"></span>
<span class="btn-calendar" aria-hidden="true"></span>
<span class="trash" aria-hidden="true"></span>
<span class="whatsapp" aria-hidden="true"></span>
```

Accesibilidad recomendada:

- Usa `aria-hidden="true"` cuando el icono sea decorativo.
- Agrega texto visible o `aria-label` en botones cuando el icono represente una
  accion.
- Evita depender solo del icono para comunicar estados criticos.

## Catalogo visual

Abre `index.html` en un navegador o sirvelo con un servidor HTTP. La galeria
carga `style_icons.css`, muestra tarjetas con cada clase y agrupa los iconos en
categorias visuales calculadas en el JavaScript de la pagina:

- Archivos y Carpetas.
- Navegacion y Acciones.
- Usuarios y Perfil.
- Estados y Validaciones.
- Comunicacion.
- Sistema y Herramientas.
- Otros.

Rutas utiles cuando el proyecto esta publicado:

| Ruta | Uso |
|---|---|
| `/` o `/index.html` | Galeria visual |
| `/style_icons.css` | Hoja de estilos consumible por otros proyectos |
| `/manifest.json` | Catalogo estructurado |
| `/icons/NOMBRE_ARCHIVO.svg` | Asset individual |
| `/icons/NOMBRE_ARCHIVO.png` | Asset individual |

## Manifest del catalogo

`manifest.json` contiene el inventario de iconos detectado desde
`style_icons.css`. Cada elemento tiene esta forma:

```json
{
  "class": "btn-save",
  "asset": "icons/btn-save.svg",
  "category": "icons",
  "format": "svg"
}
```

Estado actual del manifest:

| Dato | Valor |
|---|---:|
| Entradas en `manifest.json` | 89 |
| Assets referenciados por CSS | 89 |
| Clases CSS unicas | 89 |
| Entradas SVG en manifest | 82 |
| Entradas PNG en manifest | 7 |

Tambien existen 26 archivos dentro de `icons/` que no estan referenciados por
`style_icons.css` ni por `manifest.json` en el estado actual. Deben revisarse
antes de eliminarlos porque podrian estar reservados para uso futuro o consumo
directo:

```text
icons/b_snewtbl.png
icons/barcode.png
icons/btn-home-black.svg
icons/comedor.png
icons/edit.png
icons/elaboracion.png
icons/eliminar.png
icons/facturar.png
icons/filetype-pdf.svg
icons/filetype-xml.svg
icons/ico_left.png
icons/insumos.png
icons/link.svg
icons/mariadb.svg
icons/notificacion_error.svg
icons/notificacion_ok.svg
icons/notificacion_question.svg
icons/pagar.png
icons/pdf_icono.png
icons/productos.png
icons/recargar.png
icons/recetario.png
icons/scissors.svg
icons/sendmail.svg
icons/upload.svg
icons/xls_icono.png
```

## Validacion

Ejecuta el validador antes de publicar cambios:

```bash
python3 scripts/validate_icons.py
```

El script comprueba:

- Que cada `url(...)` en `style_icons.css` apunte a un archivo existente.
- Que no existan clases duplicadas en `style_icons.css`.
- Que cada entrada de `manifest.json` apunte a un asset existente.

El validador no comprueba actualmente:

- Que todos los archivos de `icons/` esten en el CSS o en el manifest.
- Que `index.html` incluya todas las clases del manifest.
- Que las dimensiones o estilos visuales sean consistentes.
- Que el contenido SVG/PNG sea semanticamente correcto.

Comandos utiles de revision:

```bash
python3 scripts/validate_icons.py
git diff --check
git status --short
```

## Ejecucion con Docker

El proyecto incluye `docker/docker-compose.yml` para servir la raiz del
repositorio con Apache `httpd:alpine`.

Iniciar:

```bash
docker compose -f docker/docker-compose.yml up -d
```

Abrir la galeria:

```text
http://localhost:8014/
```

Detener:

```bash
docker compose -f docker/docker-compose.yml down
```

Revisar contenedores:

```bash
docker compose -f docker/docker-compose.yml ps
```

El compose monta el repositorio con una ruta relativa para que funcione aunque
el proyecto se clone en otra ubicacion:

```yaml
volumes:
  - ../:/usr/local/apache2/htdocs/
```

## Despliegue

Como el proyecto es estatico, puede publicarse en cualquier servidor capaz de
servir HTML, CSS, JSON y archivos SVG/PNG.

Opciones compatibles:

- Apache.
- Nginx.
- GitHub Pages.
- S3 compatible con hosting estatico.
- CDN o storage estatico equivalente.
- Contenedor Apache basado en el compose incluido.

Archivos minimos para consumo por CSS:

```text
style_icons.css
icons/
```

Archivos recomendados para publicacion completa:

```text
index.html
style_icons.css
manifest.json
icons/
LICENSE
```

Recomendaciones para administradores de sistemas:

- Servir `style_icons.css`, `manifest.json`, `.svg` y `.png` con tipos MIME
  correctos.
- Usar cache con versionamiento por tag, release o ruta versionada.
- Evitar cache agresivo sobre `index.html` si se usa como galeria de revision.
- Mantener `icons/` en la misma ruta relativa esperada por `style_icons.css`.
- Publicar sobre HTTPS cuando sea consumido por aplicaciones web en produccion.

Ejemplo conceptual con Nginx:

```nginx
server {
    listen 80;
    server_name icons.example.com;
    root /var/www/core.icons;
    index index.html;
}
```

## Configuracion

No se detectan archivos `.env`, `.env.example` ni variables de entorno requeridas
por el proyecto.

| Variable | Requerida | Proposito |
|---|---|---|
| N/A | No | El proyecto no usa variables de entorno detectables. |

Configuracion detectada:

| Archivo | Parametro | Valor actual | Nota |
|---|---|---|---|
| `docker/docker-compose.yml` | Servicio | `coreicons` | Nombre del servicio Docker Compose. |
| `docker/docker-compose.yml` | Imagen | `httpd:alpine` | Servidor Apache ligero. |
| `docker/docker-compose.yml` | Puerto | `8014:80` | Expone Apache en `localhost:8014`. |
| `docker/docker-compose.yml` | Restart policy | `unless-stopped` | Reinicia salvo detencion manual. |
| `docker/docker-compose.yml` | Volumen | `../:/usr/local/apache2/htdocs/` | Monta el repositorio con ruta relativa. |
| `index.html` | Robots | `noindex,nofollow` | Evita indexacion de la galeria. |
| `index.html` | Cache-Control | `no-cache, no-store, must-revalidate` | Orientado a revision sin cache del HTML. |

## Mantenimiento

Para agregar un icono nuevo:

1. Agrega el archivo SVG o PNG en `icons/`.
2. Define una clase nueva en `style_icons.css`.
3. Agrega la entrada correspondiente en `manifest.json`.
4. Agrega o verifica la tarjeta en `index.html` si debe aparecer en la galeria.
5. Ejecuta `python3 scripts/validate_icons.py`.
6. Revisa visualmente `index.html` en navegador.

Convencion recomendada para nuevas clases:

```css
.nombre-del-icono {
  display: inline-block;
  width: 22px;
  height: 22px;
  background: url(icons/nombre-del-icono.svg) no-repeat center center;
  background-size: 22px 22px;
  margin: 0px 2px;
}
```

Buenas practicas:

- Preferir SVG para iconos escalables, salvo que exista una razon para PNG.
- Mantener nombres de clase descriptivos y estables.
- Evitar cambiar nombres de clases existentes sin revisar consumidores externos.
- Ejecutar el validador antes de hacer commit o desplegar.
- Revisar los 26 assets no referenciados antes de depurar `icons/`.
- Mantener sincronizados `style_icons.css`, `manifest.json` e `index.html`.

## Seguridad y datos sensibles

No se detectaron secretos, tokens, contrasenas, credenciales ni archivos `.env`
versionados en los archivos revisados del proyecto.

Controles aplicados:

- `.gitignore` excluye archivos `.env`, llaves privadas y archivos locales de
  herramienta.
- `docker/docker-compose.yml` usa una ruta relativa para no exponer rutas del
  equipo local.
- Los SVG no deben incluir rutas absolutas en metadata de exportacion.
- Si en el futuro se agregan credenciales para despliegue, deben vivir en
  variables de entorno, secretos del proveedor CI/CD o archivos no versionados.
- No publiques iconos o imagenes con informacion sensible incrustada en sus
  metadatos.

## Pendiente por documentar

- URL oficial del repositorio remoto.
- Proceso formal de versionamiento y publicacion de releases.
- Politica de compatibilidad para nombres de clases existentes.
- Fuente/licencia individual de cada icono, si provienen de paquetes o autores
  externos.
- Proceso automatizado para regenerar `manifest.json` desde `style_icons.css`,
  si existe fuera de este repositorio.
- Estrategia oficial de CDN/cache para produccion.
- Pruebas visuales automatizadas, si se desean para prevenir regresiones en la
  galeria.

## Licencia

Este proyecto esta licenciado bajo MIT. Consulta `LICENSE` para el texto
completo.
