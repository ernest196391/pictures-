# Pendientes y orden de avance

## Siguiente lote

- [ ] Recibir las dos nuevas fotos; todavía no recibidas al registrar esta actualización.
- [ ] Identificar productos, variantes y etiquetas CUP.
- [ ] Comparar con los 32 productos existentes; proponer reutilización solo si coincide envase, variante y tamaño.
- [ ] Crear o reutilizar imágenes revisadas, actualizar datos y publicar.
- [ ] Registrar nuevos aprendizajes y dudas.

## Datos comerciales

- [ ] Confirmar los 16 candidatos detallados en `data/coloshop/batch-001/pending.json`.
- [ ] Gain pequeño: distinguir etiquetas de 5.000 / 7.000 CUP.
- [ ] Confirmar precios compartidos de detergentes, geles y ambientadores.
- [ ] Completar presentaciones, GTIN y stock cuando exista evidencia.

## App por bloques

1. Subida desde móvil y almacenamiento de originales con hash e ID de lote.
2. Extracción OCR y candidatos por objeto con evidencia, sin publicación automática de dudas.
3. Catálogo global: producto, variante, GTIN opcional e imágenes revisadas; ofertas separadas por tienda.
4. Búsqueda de coincidencias: hash exacto, imagen parecida y reconocimiento de producto. Revisión antes de reutilizar.
5. Generación comercial con proveedor configurable y control de identidad del envase.
6. Panel para aprobar imágenes, editar precios persistentes y exportar CSV.
7. Conectores de publicación con reintentos e idempotencia.
8. Pulido móvil: Helvetica o equivalente, pocas acciones y sin información técnica en el flujo del comerciante.

## Validación pendiente

- Acceso real al panel autenticado para probar tabla y CSV; en el piloto se verificó su redirección a login, compilación y rutas.
- Prueba de compra completa con datos reales del propietario; no se creó un pedido de prueba en producción.
- Detector semántico y permisos de reutilización entre tiendas.
