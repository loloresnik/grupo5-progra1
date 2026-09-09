Descripción general

Este repositorio contiene un módulo en Python para la gestión básica de productos por consola.
Mi aporte consistió en revisar y completar funciones ya existentes, unificar el estilo de código, agregar validaciones de entrada y desarrollar un mini menú interactivo para probar el módulo. El objetivo fue aplicar conceptos vistos en la materia: listas como matriz, funciones, expresiones regulares y operaciones funcionales.

Contenido entregado

gestion_productos.py: módulo con las funciones de gestión.

main.py: script con un mini menú interactivo para probar el módulo.

Estructura de datos

Cada producto se representa como una lista con 5 elementos:
0: ID (int)
1: Nombre (str)
2: Categoria (str)
3: Proveedor (str)
4: Stock (int)

La variable principal es una lista de productos: productos = [ [id, nombre, categoria, proveedor, stock], ... ]

Funciones principales incluidas

agregar_producto(productos)
Pide datos por consola, valida con regex, convierte ID y stock a int y agrega la fila a productos. Devuelve 1 si se agregó correctamente.

buscar_producto(productos, id_prod)
Busca por ID y devuelve la fila del producto o None si no existe.

modificar_producto(productos, id_prod, nuevo_nombre=None, nueva_categoria=None, nuevo_proveedor=None)
Modifica los campos no None del producto encontrado. Devuelve 1 si se modificó, 0 si no se encontró.

eliminar_producto(productos, id_prod)
Elimina el producto con el ID indicado. Devuelve 1 si se eliminó, 0 si no existe.

mostrar_productos(productos)
Imprime la lista completa en formato tabla.

ingreso_stock(productos, id_prod, cantidad)
Suma cantidad al stock del producto. Valida existencia y cantidad positiva.

egreso_stock(productos, id_prod, cantidad)
Resta cantidad si hay stock suficiente. Valida existencia, cantidad positiva y stock disponible.

consultar_stock(productos, id_prod)
Imprime y devuelve el stock actual del producto o None si no existe.

ordenar_por_nombre(productos)
Ordena la lista productos in-place por nombre.

ordenar_por_stock(productos)
Devuelve una lista ordenada por stock (la implementación actual devuelve una lista ordenada para mostrar).

filtrar_stock_bajo(productos, limite)
Imprime productos con stock menor al límite.

mostrar_nombres(productos)
Imprime solo los nombres de los productos.

stock_total(productos)
Calcula y muestra la suma total de stock usando reduce.

Decisiones de diseño y justificación


Validaciones con expresiones regulares: se usan patrones simples y claros:


^\d+$ para campos numéricos (ID, stock)

^[A-Za-z ]+$ para campos alfabéticos con espacios (nombre, categoría, proveedor)
Esto asegura que las entradas cumplan el formato esperado y demostrar mi manejo de regex.

Uso de str.isdigit() en el menú: para validaciones rápidas en el menú interactivo use isdigit() devuelve True si la cadena contiene al menos un carácter y todos los caracteres son dígitos .

Funciones pequeñas y específicas: cada operación está encapsulada en su propia función para facilitar pruebas, lectura y corrección.

Mensajes en consola: se mantienen mensajes claros para el usuario y para la corrección manual.


Limitaciones y supuestos


No hay persistencia: los datos residen en memoria durante la ejecución. No se guarda en archivos.

IDs no autogenerados: se espera que el usuario ingrese IDs únicos; no hay verificación automática de duplicados al agregar (mejora posible).

Validaciones básicas: por simplicidad no se aceptan acentos ni caracteres especiales en nombres/categorías/proveedores.

Stock y ID son enteros positivos; no se manejan negativos ni decimales.


Casos de prueba sugeridos

Intentar agregar ID no numérico - debe pedir reingreso.

Intentar nombre con números o símbolos - debe pedir reingreso.

Ingreso/egreso de stock con cantidad negativa o mayor al disponible - debe rechazar.

Carga múltiple con formato incorrecto (menos o más campos) - debe ignorar ese grupo y procesar los demás.

Buscar, modificar y eliminar IDs existentes y no existentes.


Mejoras posibles (trabajo futuro)


Verificar unicidad de ID al agregar.

Soporte para acentos y caracteres Unicode en nombres (ajustar regex).

Persistencia en CSV o JSON y carga automática al iniciar.

Interfaz mínima gráfica o web.


Cómo ejecutar


Colocar gestion_productos.py y main.py en la misma carpeta.

Ejecutar desde consola:
python main.py

Usar el menú interactivo para probar las opciones.

Autor de este branch:
Martinez Sccasso Ivan Ricardo
