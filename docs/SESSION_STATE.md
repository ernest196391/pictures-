# Estado para retomar

Fecha: 2026-10-04. Tienda piloto: Colo Shop. App: ernest196391/pictures-; tienda: ernest196391/frutos-secos.

- Lote 001: 20 fotos, 32 productos publicados, 16 pendientes.
- Lote 002: 20 fotos, 29 productos publicados, 15 pendientes; 29 imágenes aceptadas, 45 llamadas registradas (32 en el pase aprobado y 13 anteriores sustituidas), con 3 correcciones en el pase aprobado.
- Lote 003: 20 fotos, 23 productos publicados, 24 pendientes; 23 imágenes aceptadas, 25 llamadas (2 correcciones).
- Total: 60 fotos inspeccionadas, 84 productos publicados y 55 candidatos pendientes excluidos de ventas.
- Commit tienda lote 003: 33aea696faff4d14e9c695e433b1317a356389a7. Producción https://frutos-secos-drab.vercel.app/. Despliegue dpl_F1BEEGjff8H6Sx3zPdDg4EmFwC4r READY.
- Verificación lote 003: 19 tests, compilación, catálogo 84 en navegador, imagen Macro Food Piña y carrito 1280 CUP. No se creó pedido real ni se verificó panel autenticado.
- Datos por lote: productos, pendientes, manifiesto, tabla CSV; lote 002 añade prompts. Hashes y rutas conservados para recuperar activos sin regenerar.
- No regenerar si coincide producto, variante, tamaño y envase. El detector SHA/dHash solo propone coincidencias, no identifica semánticamente productos ni los combina.
- No repartir precios compartidos, inventar volumen o cantidad. CUP; precio fuera de imagen, oferta separada por tienda.

Siguiente trabajo: confirmar pendientes, crear cargador móvil con almacenamiento persistente y catálogo global de imágenes revisadas. Panel actual consulta/exporta; no edita precios persistentes. App todavía es prototipo documentado, no flujo automático completo.

Para ahorrar: leer este archivo, procesar solo nuevos hashes, resolver precios antes de generar y solicitar una foto frontal y un precio inequívoco por producto. Priorizar quitar fondo preservando envase cuando sea viable; recreaciones necesitan revisión de cierres y etiquetas. No conocemos coste exacto de créditos.
