# my_icons

Coleccion de iconos SVG/PNG y hoja de estilos utilitaria para usarlos como clases CSS en proyectos web.

## Estructura

- `style_icons.css`: clases CSS (`.btn-save`, `.file-pdf`, etc.)
- `manifest.json`: catalogo de clases y assets
- `icons/`: todos los assets SVG/PNG en un solo directorio
- `index.html`: galeria visual
- `scripts/validate_icons.py`: validacion de integridad

## Uso en otros proyectos

```html
<link rel="stylesheet" href="https://TU-DOMINIO/my_icons/style_icons.css" />
<span class="btn-save" aria-hidden="true"></span>
```

## Validacion

```bash
python3 scripts/validate_icons.py
```

## Recomendacion de publicacion

Publica este repositorio como hosting estatico (GitHub Pages/S3+CloudFront/Nginx) y consume por version de tag (`v1.x.x`) para cache estable.

## Licencia

MIT. Ver `LICENSE`.
