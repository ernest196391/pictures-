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
