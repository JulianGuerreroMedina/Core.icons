# my_icons

Coleccion de iconos SVG/PNG y hoja de estilos utilitaria para usarlos como clases CSS en proyectos web.

## Que es este repositorio

Este repo funciona como una mini libreria de iconografia:

- `style_icons.css` mapea clases CSS (por ejemplo `.btn-save`) a archivos de imagen (`btn-save.svg`).
- `index.html` sirve como galeria visual y ejemplo de uso.
- Los archivos `.svg` y `.png` son los assets consumidos por las clases.

No hay build step, backend ni JavaScript de aplicacion: es un paquete estatico.

## Estructura del proyecto

El repositorio vive practicamente en un solo nivel (sin subcarpetas funcionales):

- `index.html`: entry point de demostracion y catalogo visual de iconos.
- `style_icons.css`: definicion de clases reutilizables y sprites (semaforo).
- `README.md`: documentacion del proyecto.
- `*.svg` y `*.png`: assets de iconos.
- `.git/`: metadatos de versionado.

### Jerarquia resumida

```txt
my_icons/
├── index.html
├── style_icons.css
├── README.md
├── *.svg
├── *.png
└── .git/
```

## Flujo de funcionamiento

### Entry point

`index.html` es el punto de entrada para visualizar la libreria. Carga `style_icons.css` desde el `<head>`.

### Flujo de datos (render)

1. El navegador parsea `index.html`.
2. Se carga `style_icons.css`.
3. Cada `<span class="...">` toma su regla CSS correspondiente.
4. La regla aplica `background: url(<icono>) ...`.
5. El navegador resuelve el archivo SVG/PNG y lo renderiza.

### Logica de negocio

No existe logica de negocio programatica (sin JS, sin funciones de dominio, sin estado).
La “logica” de este repo es de presentacion:

- convencion de nombres de clases,
- mapeo clase -> asset,
- tamanos y offsets de iconos (incluye sprite `semaforo.svg`).

## Diccionario de funciones/metodos clave

Este proyecto no define funciones ni metodos de lenguaje (JavaScript/TypeScript/PHP/etc.).

Para documentar las unidades clave reales, aqui va un diccionario de clases CSS reutilizables:

| Unidad | Entrada | Salida | Responsabilidad |
| --- | --- | --- | --- |
| `.btn-file`, `.btn-save`, `.btn-user`, etc. | Un elemento HTML con esa clase (normalmente `<span>`) | Render de icono via `background-image` | Pintar iconos de accion comunes |
| `.file-audio`, `.file-pdf`, `.file-xls`, etc. | Elemento con clase de tipo de archivo | Icono de archivo en 120x120 | Representar tipos de archivo |
| `.notificacion_error`, `.notificacion_ok`, etc. | Elemento con clase de estado | Icono de notificacion (64x64) | Visualizar estados de feedback |
| `.a-tiempo`, `.por-vencer`, `.cumplio-despues`, etc. | Elemento con clase de estado semaforo | Seccion de sprite con `background-position` | Mostrar estados temporales usando `semaforo.svg` |
| `.contenedor-iconos`, `.contenedor-files`, `.iconos` (en `index.html`) | Bloques HTML de galeria | Layout en cuadricula flotante | Organizar visualmente el catalogo |

## Stack tecnologico

- HTML5
- CSS3
- Assets SVG y PNG
- Git para control de versiones
- Navegador moderno (Chrome/Firefox/Edge/Safari) para visualizacion

### Dependencias externas

No usa dependencias de NPM, Composer ni CDN.

## Instalacion y configuracion

### Requisitos

- Git (opcional, para clonar)
- Navegador web

### Setup local

```bash
git clone <tu-fork-o-este-repo>
cd my_icons
```

No hay instalacion adicional.

## Uso

### 1) Vista de galeria

Abre `index.html` en tu navegador para inspeccionar el catalogo completo.

### 2) Reusar en otro proyecto

1. Copia `style_icons.css` y los iconos que necesites.
2. Importa la hoja de estilos.
3. Usa la clase del icono en un elemento inline.

```html
<link rel="stylesheet" href="style_icons.css" />
<button type="button">
  <span class="btn-save" aria-hidden="true"></span>
  Guardar
</button>
```

### 3) Agregar un icono nuevo

1. Coloca el archivo (ej. `btn-new.svg`) en la raiz del repo.
2. Agrega su clase en `style_icons.css`.
3. (Opcional) Agrega una tarjeta en `index.html` para previsualizarlo.

```css
.btn-new {
  display: inline-block;
  width: 22px;
  height: 22px;
  background: url(btn-new.svg) no-repeat center center;
  background-size: 22px 22px;
  margin: 0 2px;
}
```

## Convenciones recomendadas

- Nombres consistentes con prefijos semanticos: `btn-*`, `file-*`, `notificacion_*`.
- Mantener tamanos estandar por familia de iconos (22x22, 32x32, 64x64, 120x120).
- Evitar duplicados (hay variantes legacy con sufijos como `____` que conviene depurar gradualmente).

## Contribucion (guia minima)

1. Haz un fork y crea una rama descriptiva.
2. Agrega/modifica iconos y su clase en `style_icons.css`.
3. Actualiza `index.html` si aplica para mostrar el nuevo icono.
4. Verifica visualmente en navegador que no haya rutas rotas.
5. Abre un Pull Request con:
   - objetivo del cambio,
   - iconos agregados/modificados,
   - captura de pantalla de la galeria (si aplica).

## Licencia

No se declara una licencia explicita en este repositorio.
Si planeas distribuir o reutilizar los assets, define y agrega un archivo `LICENSE`.
