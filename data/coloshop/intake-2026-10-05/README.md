# Colo Shop: revisión parcial de los ZIP 0 y 1

Se revisaron las 142 imágenes de los dos ZIP: 34 son las mismas tomas de lotes anteriores, ahora con mayor resolución o distinta compresión; 108 son tomas nuevas. La coincidencia anterior se comprobó por nombre y huella visual de 256 bits (distancia de 0 a 8), no por nombre solamente. Los originales tienen distinta huella binaria de las versiones recibidas anteriormente.

El catálogo publicado conserva 150 productos. Esta auditoría no añade productos ni genera imágenes. Faltan dos ZIP para cerrar el inventario de la sesión.

## Archivos de trabajo

- `control-fotos.csv` / `photos.json`: ZIP, ruta dentro del archivo, nombre, SHA256, dimensiones, revisión, coincidencias y vínculos a productos.
- `productos-por-hacer.csv` / `candidate-products.json`: 159 fichas de trabajo observadas en las tomas nuevas; 157 no tienen registro publicado y dos enriquecen pendientes anteriores. Algunas fichas agrupan familias cuya presentación exacta aún debe separarse, y una familia de maní tiene posibles coincidencias con pendientes previos. No equivalen a 159 SKU terminados.
- `inventario-maestro.csv` / `master-products.json`: 388 registros de trabajo: 150 publicados, 81 pendientes previos (dos enriquecidos sin duplicarlos) y 157 candidatos adicionales. Las categorías de pendientes que no la almacenaban se proponen por el nombre y están marcadas como tales.
- `pending-review.json`: precios dudosos o faltantes y detalles pendientes de identificación, peso o unidad.
- `weighed-pack-observations.json`: peso/precio de nueve porciones individuales; no representa existencias ni establece una tarifa por kilogramo.
- `manifest.json`: estado, procedencia de los ZIP, huellas y commits usados como referencia.
- `categories.json`: categorías actuales con subcategorías propuestas para el futuro panel.
- `SYSTEM.md`: entidades, reglas y cola para el sistema de escritorio.

## Precios

107 fichas tienen un precio asignado legible en foto; 25 tienen cartel compartido; 14 carecen de precio; dos muestran conflicto entre tomas; tres requieren asociación o separación de tamaños; ocho se venden por peso o presentación variable. `direct` significa lectura visual, no confirmación de vigencia por el propietario. Un precio compartido, conflictivo o variable nunca se carga como `priceCUP` fijo.

Se completó evidencia para frijoles negros Del Campo (bolsa de 1 lb, 1.600 CUP) y arroz Alfinete (1 kg, 1.300 CUP), ambos pendientes anteriores. La tienda aún no se modifica; estas observaciones están preparadas para el próximo trabajo.

Casos que deben resolverse: Tropi Gusto mango/banana aparece con 600 y 800 CUP (pueden ser tamaños diferentes); Havana Club 7 años tiene dos tamaños/precios (10.200/11.900) sin volumen confirmado; varias aguas tienen marca o asociación dudosa. Las familias Bahamas/Bali deben separarse por sabor y volumen. No deducir stock contando envases de las fotos.

## Siguiente paso con los ZIP 2 y 3

1. Registrar cada miembro por SHA256 y comparar su imagen con las tomas ya recibidas.
2. Vincular nuevos detalles/precios al identificador existente; comprobar marca, variante y presentación antes de crear otro producto.
3. Resolver campos dudosos con las fotos adicionales. Mantener evidencia y lecturas anteriores si aparece un conflicto.
4. Reservar imágenes comerciales solo para SKU identificados que no tengan imagen aprobada; ejecutar por lotes, con registro de trabajo y revisión visual.
5. Publicar los productos completos, con precio CUP y trazabilidad; los demás siguen en revisión.

Los originales permanecen en los dos ZIP adjuntos. El manifiesto guarda sus identificadores autorizados y cada ruta interna para poder recuperarlos. No cambiar ni sobrescribir los archivos del usuario.
