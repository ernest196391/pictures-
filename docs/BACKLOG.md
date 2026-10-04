# Pendientes y orden de avance

## Siguiente lote

- [x] Recibir nuevo lote: llegaron 20 fotos adicionales, inspeccionadas y registradas en batch-002.
- [x] Identificar segundo lote: 29 productos listos para imagen y 15 dudas de precio/presentación.
- [x] Comparar con los 32 existentes: sin coincidencias exactas aprobadas en este lote.
- [x] Crear 29 imágenes revisadas y actualizar catálogo; commit tienda 0cb84c39d29aad736da1bcde58a213920c399906. Verificar despliegue en SESSION_STATE.
- [x] Registrar aprendizajes y dudas; 3 correcciones documentadas.

## Datos comerciales

- [ ] Confirmar los 15 candidatos de `data/coloshop/batch-002/pending.json` (31 pendientes acumulados).

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
