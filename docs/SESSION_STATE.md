# Estado para retomar

Fecha: 2026-10-04. Tienda piloto: Colo Shop. App: ernest196391/pictures-; tienda: ernest196391/frutos-secos.

- Lote 001: 20 fotos, 32 productos publicados, 16 pendientes.
- Lote 002: 20 fotos, 29 productos publicados, 15 pendientes; 29 imágenes aceptadas, 45 llamadas registradas (32 en el pase aprobado y 13 anteriores sustituidas), con 3 correcciones en el pase aprobado.
- Lote 003: 20 fotos, 23 productos publicados, 24 pendientes; 23 imágenes aceptadas, 25 llamadas (2 correcciones).
- Lote 004: 20 archivos: 14 duplicados exactos reutilizados y 6 fotos nuevas; 20 productos nuevos y 11 pendientes; 21 llamadas de imagen, incluida una corrección de peso no legible.
- Lote 005: 14 fotos nuevas; 17 productos y 9 candidatos pendientes; Mascotas añadida para HappyOne 4 kg.
- Total: 114 archivos recibidos, 100 fotos únicas inspeccionadas, 150 productos y 81 candidatos pendientes excluidos de ventas.
- Commit tienda lote 003: 33aea696faff4d14e9c695e433b1317a356389a7. Producción https://frutos-secos-drab.vercel.app/. Despliegue dpl_F1BEEGjff8H6Sx3zPdDg4EmFwC4r READY.
- Verificación lote 003: 19 tests, compilación, catálogo 84 en navegador, imagen Macro Food Piña y carrito 1280 CUP. No se creó pedido real ni se verificó panel autenticado.
- Datos por lote: productos, pendientes, manifiesto, tabla CSV; lote 002 añade prompts. Hashes y rutas conservados para recuperar activos sin regenerar.
- No regenerar si coincide producto, variante, tamaño y envase. El detector SHA/dHash solo propone coincidencias, no identifica semánticamente productos ni los combina.
- No repartir precios compartidos, inventar volumen o cantidad. CUP; precio fuera de imagen, oferta separada por tienda.

Siguiente trabajo: confirmar pendientes, crear cargador móvil con almacenamiento persistente y catálogo global de imágenes revisadas. Panel actual consulta/exporta; no edita precios persistentes. App todavía es prototipo documentado, no flujo automático completo.

Para ahorrar: leer este archivo, procesar solo nuevos hashes, resolver precios antes de generar y solicitar una foto frontal y un precio inequívoco por producto. Priorizar quitar fondo preservando envase cuando sea viable; recreaciones necesitan revisión de cierres y etiquetas. No conocemos coste exacto de créditos.

Lote 004 publicado: bd0c33ae7570ccdb696c42fedb0aab428bc2b3b8; despliegue dpl_8MTasJUohXMTZ3iA3u5JrGJcAV43 READY. Verificado catálogo 104, imagen Wellsley 900 px y subtotal 19500 CUP; carrito de prueba retirado. No regenerar este lote.

Lote 005 publicado: c513a6bbac564ad5e2720b9075b69eff1c84e819; despliegue dpl_ARLyW1yRrcVxmP4hf82R58zKvprf READY. Verificados 19 tests, compilación, catálogo 121, Mascotas, imagen HappyOne 900 px y subtotal 18700 CUP; carrito de prueba retirado sin crear pedido. No regenerar este lote.

Lote 006: 20 fotos nuevas; 29 productos, 7 pendientes nuevos y 1 pendiente anterior resuelto (La Sota Alcaparras). Tres pestos publicados reutilizados. Imágenes revisadas y publicadas; reutilizar los activos aprobados.

Lote 006 publicado: 78327ff225389b75de7007e977da7f2e00948cd3; despliegue dpl_8K6jeXScNyzWPZZoruHk2QzXVjnN READY. Verificados 19 tests, compilación, catálogo 150, categoría Bebidas con 4 productos, imagen Coca-Cola 900 px y subtotal 1200 CUP; carrito de prueba retirado sin pedido. 29 imágenes aprobadas en 29 llamadas, sin correcciones. No regenerar este lote.


## 2026-10-05: auditoría parcial ZIP0 y ZIP1

142 fotos:34 tomas previas recomprimidas y108 nuevas.159 fichas candidatas (157 adicionales y2 pendientes previos enriquecidos);107 con precio legible. Catálogo sigue150 publicados. Sin generación de imágenes ni cambios en tienda. Faltan2ZIP. Fuente autoritativa de la sesión: `data/coloshop/intake-2026-10-05/README.md`, `manifest.json`, `photos.json` y `master-products.json`. Revisar estas fichas antes de reservar batch007; incluyen familias y precios por peso, no todos son SKU finalizados.
