# Auditoría de fotos Colo Shop

Los cuatro ZIP recibidos están revisados:297 fotos,100 tomas ya inspeccionadas y197 tomas nuevas. No quedan ZIP pendientes de este lote.

`master-products.csv` y JSON contienen150 fichas publicadas y las observaciones pendientes. Las filas de familias, posibles coincidencias y formatos sin confirmar no son SKU finales. `pending-review.csv` indica la siguiente acción. `photos.csv` permite localizar cada toma dentro de su ZIP, evitar repetir trabajo y consultar su SHA256.

Un precio directo significa que se leyó el cartel asociado en la fotografía; no confirma vigencia actual. Un cartel compartido, borroso, contradictorio o precio variable no se carga como precio fijo. Fotos de cajas expositoras no establecen automáticamente que se venda la caja entera. No se infiere stock de las fotos.

Se conservaron los150 productos publicados. No se generaron nuevas imágenes ni se modificó la tienda. Los originales se recuperan de los ZIP del usuario usando el nombre de archivo y miembro registrados en el manifiesto. La cobertura es completa para estos cuatro ZIP; no puede garantizarse que sean todas las fotos existentes en la PC sin comparar con un listado de la carpeta original.

Conteos detallados en `summary.json`; categorías en `categories.json`; requisitos del sistema en `SYSTEM.md`.
