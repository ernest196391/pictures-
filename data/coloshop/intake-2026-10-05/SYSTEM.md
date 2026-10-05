# Requisitos obtenidos de la revisión para Pictures

## Entidades mínimas

| Entidad | Clave | Datos |
|---|---|---|
| Archivo de origen | SHA256 | Archivo ZIP, miembro, nombre original, dimensiones, huella visual y estado de revisión |
| Producto | ID estable | Nombre, marca y variante verificadas, categoría, subcategoría, descripción y evidencia |
| Presentación | Producto + tamaño + envase | Unidad de venta, cantidad, peso o volumen, precio, moneda y evidencia propia |
| Lectura de precio | ID de observación | Foto, valor leído, asociación, confianza, conflicto y confirmación del dueño |
| Porción pesada | ID de unidad futura | Producto, peso real, precio individual, stock y estado de venta; las fotos actuales solo son observaciones |
| Imagen comercial | Producto/presentación | Fuente, prompt, estado, hash aprobado y URL; reutilización entre tiendas |
| Trabajo | ID idempotente | Estado reservado, generando, revisando, aprobado o publicado; reintentos sin duplicar |

## Reglas de operación

- Importar carpetas y ZIP desde el equipo; escanear primero y mostrar balance antes de generar imágenes.
- Distinguir archivo idéntico, foto recomprimida y toma distinta del mismo producto. El parecido por sí solo no confirma identidad comercial.
- Buscar por ID, nombre, marca, categoría, archivo y estado. Filtrar publicados, pendientes, faltantes de imagen y precios por confirmar.
- Nombre, sabor, envase y tamaño determinan la presentación; un cambio de sabor no hereda automáticamente el precio.
- Mostrar el recorte del producto y su cartel junto al campo precio. Guardar precio de producto y precio observado como campos distintos.
- Nunca convertir un cartel compartido en varios precios confirmados sin evidencia o confirmación.
- Precio fijo de paquete y precio de porción pesada son modos distintos. La tarifa/kg es un campo separado que requiere confirmación; no calcularla de etiquetas redondeadas.
- Stock desconocido queda nulo; cantidad de envases visibles no es inventario contable.
- Etiquetas de vencimiento o fecha del nombre de foto no establecen fecha de captura ni vigencia.
- Reusar imágenes aprobadas. Registrar reserva antes de generar; impedir generación para el mismo producto cuando existe trabajo activo o imagen aprobada.
- Publicación exige revisión de marca, variante, tamaño, unidad y precio. Guardar el commit y comprobar la URL resultante.

## Alcance de esta entrega

Es una base de datos y especificación para continuar el sistema. No implementa todavía el importador de escritorio, venta por peso, inventario físico ni panel de corrección. Los CSV/JSON están listos para usar como insumos de esos módulos. La tienda publicada conserva su catálogo anterior.


## Cierre de los cuatro ZIP

Importación idempotente por SHA256 y nombre, con coincidencia perceptual para reencodificaciones. Guardar relación foto-producto y evidencia separada del precio. Bloquear publicación de familias sin separar y coincidencias posibles; confirmar unidad de venta (sobre, bolsa, caja, kilogramo) y presentación. Mantener precios compartidos o borrosos como candidatos, nunca como precio fijo. Separar auditoría, aprobación de imagen y publicación. Para comprobar fotos faltantes en la PC se necesita un listado de esa carpeta;297 archivos recibidos no prueban cobertura de una carpeta no accesible.
