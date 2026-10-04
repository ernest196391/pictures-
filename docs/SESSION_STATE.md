# Estado para retomar

Fecha: 2026-10-04. Tienda piloto: Colo Shop. App: ernest196391/pictures-; tienda: ernest196391/frutos-secos.

- Lote 001: 20 fotos, 32 productos publicados, 16 pendientes.
- Lote 002: 20 fotos, 29 productos publicados, 15 pendientes; 29 imágenes aceptadas, 32 llamadas y 3 correcciones.
- Total: 40 fotos inspeccionadas, 61 productos publicados y 31 candidatos pendientes excluidos de ventas.
- Commit tienda: 0cb84c39d29aad736da1bcde58a213920c399906. Despliegue dpl_9LEqMC1kd8ywpJkhSNCxAeJPpDDh READY; producción https://frutos-secos-drab.vercel.app/.
- Verificación: 19 tests, compilación, catálogo 61 en navegador, imágenes Parex S/M y carrito 1750 CUP. No se creó pedido real ni se verificó panel autenticado.
- Datos por lote: productos, pendientes, manifiesto, tabla CSV; lote 002 añade prompts. Hashes y rutas conservados para recuperar activos sin regenerar.
- No regenerar si coincide producto, variante, tamaño y envase. El detector SHA/dHash solo propone coincidencias, no identifica semánticamente productos ni los combina.
- No repartir precios compartidos, inventar volumen o cantidad. CUP; precio fuera de imagen, oferta separada por tienda.

Siguiente trabajo: confirmar pendientes, crear cargador móvil con almacenamiento persistente y catálogo global de imágenes revisadas. Panel actual consulta/exporta; no edita precios persistentes. App todavía es prototipo documentado, no flujo automático completo.

Para ahorrar: leer este archivo, procesar solo nuevos hashes, resolver precios antes de generar y solicitar una foto frontal y un precio inequívoco por producto. Priorizar quitar fondo preservando envase cuando sea viable; recreaciones necesitan revisión de cierres y etiquetas. No conocemos coste exacto de créditos.
