# Sistema de Gestión de Inventarios

Trabajo Práctico de Programación 1 — UADE, grupo 5, 2C 2026.

## Descripción

Sistema de gestión de inventarios desarrollado en Python. Permite administrar productos, stock, movimientos, proveedores, categorías y ventas, además de generar reportes y estadísticas. Toda la información se guarda en archivos (JSON y TXT), así que se conserva cuando se cierra el programa.

El sistema cuenta con un inicio de sesión que diferencia entre **administrador** y **usuario**, con un máximo de 3 intentos. El administrador dispone además de la gestión de empleados.

## Cómo ejecutarlo

```bash
python TPO/MainP.py
```

Usuarios iniciales: `admin` / `1234` (administrador) y `usuario` / `1234`.

## Cómo correr las pruebas

```bash
cd TPO
python -m unittest -v
```

También se pueden ejecutar desde el menú principal, con la opción **9. Ejecutar pruebas**.

## Funcionalidades

- ABM, listado y consulta de productos, proveedores y empleados.
- Ingreso de stock y registro de ventas, ambos guardados como movimientos.
- Búsquedas relacionadas: los movimientos y las ventas de un producto, y los productos y el stock de un proveedor.
- Categorías: listado, productos por categoría y categorías sin ventas.
- Estadísticas: resumen estadístico, promedio general y por categoría, conteos totales y por categoría o proveedor, porcentajes, máximos y mínimos de precio y stock, y valor del inventario.
- Guardado y lectura de archivos, más la ejecución de las pruebas unitarias desde el menú.

## Estructura del proyecto

| Archivo | Contenido |
|---|---|
| `MainP.py` | Programa principal: carga los datos e inicia la sesión |
| `menu.py` | Login y todos los menús |
| `gestion_productos.py` | Productos, categorías y movimientos |
| `proveedores.py` | Proveedores (matriz) y su relación con los productos |
| `Reporte.py` | Ventas, reportes y estadísticas |
| `empleados.py` | Usuarios y empleados |
| `validaciones.py` | Expresiones regulares y entrada de datos con excepciones |
| `archivos.py` | Lectura y escritura de archivos JSON y TXT |
| `test_inventario.py` | Pruebas unitarias (`unittest`) |
| `datos/` | `productos.json`, `ventas.json`, `usuarios.json`, `proveedores.txt`, `movimientos.txt` |

## Dónde se usa cada tema

| Tema | Dónde |
|---|---|
| Diccionarios | `productos` `{id: {...}}`, `ventas` `{id: cantidad}`, `usuarios` `{usuario: {...}}`, y estadísticas por categoría |
| Matrices | `proveedores` `[id, nombre, telefono, mail]` y `movimientos` `[tipo, id, cantidad, fecha]` |
| Tuplas | Fecha `(dia, mes, anio)`, sesión `(usuario, rol)`, `TIPOS_MOVIMIENTO`, `ROLES`, `DIAS_POR_MES`, ranking `(cantidad, nombre)` y precios `(min, max, promedio)` |
| Conjuntos | Categorías únicas, proveedores sin productos (diferencia), vendidos sin stock (intersección), categorías sin ventas e IDs repetidos al leer el TXT |
| Cadenas | f-strings, `strip`/`lower`/`upper`, rebanadas (`nombre[:18]`, `capitalizar`, código de categoría, mail enmascarado), operador `in` |
| Lambda | `map` (precios con IVA), `filter` (productos sin stock), `reduce` (valor del inventario) |
| Expresiones regulares | `validaciones.py`: texto con tildes y ñ, mail, teléfono y fecha con grupos; `re.escape` en la búsqueda de proveedores |
| Excepciones | `validaciones.convertir_entero/float/fecha`, `raise ValueError` en las altas y bajas, `try/except` en todos los menús, `FileNotFoundError` y `JSONDecodeError` en `archivos.py` |
| Archivos | JSON: productos, ventas y usuarios. TXT: proveedores y movimientos. Se guarda después de cada cambio |
| Recursividad | `proveedores.buscar_proveedor_recursivo`, `Reporte.valor_total_recursivo`, `Reporte.extremo_recursivo` (máximos y mínimos) y `gestion_productos.contar_movimientos_recursivo` |
| Pruebas unitarias | `test_inventario.py`: altas, búsquedas, validaciones, cálculos y archivos |

## Integrantes

| Integrante | Legajo |
|---|---:|
| Iván Ricardo Martínez Sccasso | 1223079 |
| Lorenzo Resnik | 1215403 |
| Franco Schwab | 1238148 |
| Damián Siles | 1238437 |
| Simón Ignacio Marinucci | — |

**Scrum Master:** Lorenzo Resnik

## Recursos

- **Repositorio:** https://github.com/loloresnik/grupo5-progra1
- **Video de presentación:** https://youtu.be/ZnmKXiAl1yw
- **Video de funcionamiento:** https://youtu.be/UmUBWy5wKCc

## Objetivo

Aplicar los contenidos de Programación 1 mediante el desarrollo de un sistema modular para gestionar un inventario de forma organizada, con validaciones, estructuras de datos, persistencia en archivos, pruebas unitarias, distintos niveles de acceso y reportes.
