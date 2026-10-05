# Pictures

Herramienta en construcción: de fotos de tienda a productos revisados, imágenes comerciales y ofertas publicadas en varias tiendas.

## Estado actual

Piloto Colo Shop: 114 archivos recibidos (100 fotos únicas), 150 productos incorporados con precios CUP y 81 candidatos pendientes. El primer catálogo se publicó en `ernest196391/frutos-secos`, commit `96d944767743ce647ac20e4d5deeec678be3b837`.

- Datos y evidencia: `data/coloshop/batch-001/`  , `batch-002/` `batch-003/` `batch-004/` `batch-005/` y `batch-006/`.
- Continuidad: [SESSION_STATE](docs/SESSION_STATE.md).
- Proceso: [WORKFLOW](docs/WORKFLOW.md).
- Aprendizajes: [LEARNINGS](docs/LEARNINGS.md).
- Próximos pasos: [BACKLOG](docs/BACKLOG.md).
- Código funcional: índice SHA-256 y dHash con sugerencias de duplicados; nunca combina productos automáticamente.

```sh
python -m pip install -r requirements.txt
python src/index_images.py carpeta_fotos --output indice.json
python -m unittest discover -s tests
```

Las imágenes comerciales y las copias de consulta de los originales están versionadas en el repo de la tienda. Los manifiestos conservan sus rutas y hashes. Evitamos duplicar la base de imágenes en este repositorio; la futura aplicación deberá gestionarla con almacenamiento propio y permisos por tienda.

Todavía no están implementados el cargador móvil, OCR automático, reconocimiento de productos, generación automática, panel editable ni conectores de publicación. La generación y revisión del piloto se realizaron con asistencia humana.


### Inventario parcial desde ZIP (2026-10-05)

[Revisión de ZIP0 y ZIP1](data/coloshop/intake-2026-10-05/README.md):142 fotos,34 tomas previas y108 nuevas; inventario CSV/JSON y requisitos del sistema. Faltan dos ZIP; aún no se publican estos candidatos.
