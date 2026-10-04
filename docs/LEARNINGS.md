# Aprendizajes del piloto

## 2026-10-04 · Lote 001

1. Una foto puede contener varios productos: 20 fotos no equivalen a 20 fichas.
2. Un cartel compartido puede corresponder a varias presentaciones. Registrar candidatos y dudas; no repartir el precio automáticamente.
3. La generación puede inventar elementos del envase. Se corrigió un dispensador añadido a la crema S’nonas y un peine que se había convertido en multipack. La revisión debe comparar cantidad, cierre, silueta, variante y etiqueta.
4. Separar producto global e imagen de la oferta de cada tienda. La imagen puede reutilizarse; el precio y el stock son propios de cada tienda.
5. dHash encuentra fotos casi idénticas, no identifica por sí solo productos dentro de estanterías ni vistos desde otro ángulo.
6. Mantener hashes de los originales antes de reducirlos. Las copias públicas comprimidas son evidencia de consulta, no originales de archivo.
7. Los IDs nuevos evitan que un carrito antiguo compre otro producto al reemplazar el catálogo de demostración.
8. Los importes del carrito deben comprobarse contra el catálogo en el servidor. La ruta de pedidos de la tienda ya rechaza IDs antiguos y precios alterados; no sustituye una auditoría completa del backend público.

## Regla para cada nuevo lote

Registrar origen, observaciones, decisión, imagen utilizada, precio confirmado, pendientes y commit de publicación. Añadir fallos observados y correcciones a este documento; no presentar decisiones manuales como automatización.

## Lote 002 · 2026-10-04

- Los avisos de archivo inexistente no significaban pérdida de archivos: se verificaron y abrieron las 20 fotos en el espacio de trabajo.
- Una hoja de contacto permite ordenar el lote, pero las cifras se revisan en cada original: 1.750 de Parex S y 21.500 de Dawn no deben transcribirse como 1.450 o 2.150.
- Etiquetas plegadas, cifras ambiguas y precio por unidad frente a multipack se registran como dudas.
- Variantes cercanas y recarga frente a pulverizador son productos distintos: no reutilizar imagen ni repartir precio automáticamente.
- Consolidar apariciones repetidas dentro del lote antes de generar. Estado y contador de llamadas deben guardarse para poder reanudar.

## Cierre de imágenes del lote 002

29 imágenes aceptadas, 32 llamadas: 29 iniciales y 3 correcciones (tapón multiusos y dos Parex que salieron como surtido). No conocemos el coste real en créditos. Especificar una sola unidad y describir el cierre exacto reduce errores; comprobar contra el original antes de publicar. Las imágenes son recreaciones, no prueba del texto pequeño del envase. Mantener precios y ofertas por tienda separados del activo global.

Para la próxima sesión: cargar los originales en una sola carpeta persistente, leer SESSION_STATE, procesar solo archivos nuevos por hash, revisar identidad/precio antes de generar y reutilizar activos aprobados únicamente si coinciden variante, tamaño y envase. Una fotografía frontal por producto y otra del precio evita ambigüedades.
