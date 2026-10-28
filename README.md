# Sistema de Gestión de Inventarios

Trabajo Práctico de Programación 1 — UADE, grupo 5, 2C 2026.

## Descripción

Sistema de gestión de inventarios desarrollado en Python. Permite administrar productos, stock, movimientos, proveedores, categorías y ventas, además de generar reportes y estadísticas. Toda la información se guarda en archivos (JSON y TXT), así que se conserva cuando se cierra el programa.

El sistema cuenta con un inicio de sesión que diferencia entre **administrador** y **usuario**, con un máximo de 3 intentos. El administrador dispone además de la gestión de empleados.

## Cómo ejecutarlo

Hay que ejecutarlo **desde la carpeta `TPO`**, porque los archivos de datos (`productos.json`, `proveedores.txt`, etc.) se leen y se guardan en la carpeta desde donde se ejecuta el programa:

```bash
cd TPO
python MainP.py
```

Usuarios iniciales: `admin` / `1234` (administrador) y `usuario` / `1234`.

## Funcionalidades

- ABM, listado y consulta de productos, proveedores y empleados.
- Ingreso de stock y registro de ventas, ambos guardados como movimientos.
- Búsquedas relacionadas: los movimientos y las ventas de un producto, y los productos y el stock de un proveedor.
- Categorías: listado, productos por categoría y categorías sin ventas.
- Estadísticas: resumen estadístico, promedio general y por categoría, conteos totales y por categoría o proveedor, porcentajes, máximos y mínimos de precio y stock, y valor del inventario.
- Guardado y lectura de archivos desde el menú.

## Estructura del proyecto

| Archivo | Contenido |
|---|---|
| `MainP.py` | Programa principal: carga los datos e inicia la sesión |
| `menu.py` | Login, todos los menús e ingreso de datos con `try/except` |
| `gestion_productos.py` | Productos, categorías y movimientos |
| `proveedores.py` | Proveedores (matriz), su relación con los productos y las validaciones con expresiones regulares |
| `Reporte.py` | Ventas, reportes y estadísticas |
| `empleados.py` | Usuarios y empleados |
| `archivos.py` | Lectura y escritura de archivos JSON y TXT |
| Archivos de datos | `productos.json`, `ventas.json`, `usuarios.json`, `proveedores.txt`, `movimientos.txt` |

## Dónde se usa cada tema

| Tema | Dónde |
|---|---|
| Diccionarios | `productos` `{id: {...}}`, `ventas` `{id: cantidad}`, `usuarios` `{usuario: {...}}`, y estadísticas por categoría |
| Matrices | `proveedores` `[id, nombre, telefono, mail]` y `movimientos` `[tipo, id, cantidad, fecha]` |
| Tuplas | Fecha `(dia, mes, anio)`, sesión `(usuario, rol)`, tipos de movimiento `("Ingreso", "Egreso")`, roles, días de cada mes, ranking `(cantidad, nombre)` y precios `(min, max, promedio)` |
| Conjuntos | Categorías únicas, proveedores sin productos (diferencia), vendidos sin stock (intersección), categorías sin ventas (diferencia) e IDs repetidos al leer el TXT |
| Cadenas | f-strings, `strip`/`lower`/`upper`, rebanadas (`nombre[:18]`, `capitalizar`, código de categoría, mail enmascarado), operador `in` |
| Lambda | `map` (precios con IVA), `filter` (productos sin stock), `reduce` (valor del inventario) |
| Expresiones regulares | `proveedores.py`: nombre con tildes y ñ, teléfono y mail; `menu.py`: formato de fecha dd/mm/aaaa |
| Excepciones | `try/except` al convertir los números en `menu.py`, `raise ValueError` en las altas, bajas y modificaciones, `try/except` en todos los menús, `FileNotFoundError` y `ValueError` en `archivos.py` |
| Archivos | JSON: productos, ventas y usuarios. TXT: proveedores y movimientos. Se guarda después de cada cambio |
| Recursividad | `proveedores.buscar_proveedor_recursivo`, `Reporte.valor_total_recursivo`, `Reporte.extremo_recursivo` (máximos y mínimos) y `gestion_productos.contar_movimientos_recursivo` |

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

Aplicar los contenidos de Programación 1 mediante el desarrollo de un sistema modular para gestionar un inventario de forma organizada, con validaciones, estructuras de datos, persistencia en archivos, recursividad, distintos niveles de acceso y reportes.
