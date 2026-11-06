Sistema de Gestión de Inventarios

Trabajo Práctico de Programación 1 — UADE, grupo 5, 2C 2026.

Descripción

Sistema de gestión de inventarios para un local de venta de productos de computación, desarrollado en Python. Permite administrar productos, stock, movimientos, proveedores, categorías y ventas, además de generar reportes y estadísticas.

El sistema cuenta con un inicio de sesión que diferencia entre administrador y usuario. El administrador dispone además de funciones para realizar el alta y baja de empleados.

Los datos se guardan en archivos de texto (TXT) y JSON, por lo que se conservan entre una ejecución y otra.

Funcionalidades
Alta, baja, búsqueda, modificación y consulta de productos.

Gestión de stock y movimientos (ingresos y egresos con fecha).

Gestión de proveedores, relacionados con los productos por ID.

Gestión y consultas de categorías.

Registro de ventas con control del stock disponible.

Reportes y estadísticas: más y menos vendidos, recaudación, valores máximos y mínimos, valor total del stock, conteos, promedios y porcentajes por categoría y por proveedor, y resumen estadístico.

Inicio de sesión con distintos niveles de acceso y un máximo de 3 intentos.

Alta y baja de empleados.

Guardado de todos los datos en archivos TXT y JSON.

Validaciones de datos y manejo de errores con try/except.

Estructura del proyecto

Módulos (carpeta TPO/)
MainP.py: programa principal. Carga los datos desde los archivos y coordina el inicio de sesión y los menús.

menu.py: menús del sistema. Solo muestra las opciones y llama a las funciones de cada módulo.

gestion_productos.py: gestión de productos, stock y movimientos.

proveedores.py: gestión de proveedores.

Reporte.py: ventas, reportes y estadísticas.

empleados.py: inicio de sesión y gestión de empleados y usuarios.

validaciones.py: funciones para pedir y validar datos ingresados por el usuario.

Archivos de datos (carpeta TPO/)

Archivo	Contenido	Estructura en el programa
proveedores.txt	Proveedores (id;nombre;telefono;mail)	Matriz (lista de listas)
movimientos.txt	Ingresos y egresos (tipo;id_producto;cantidad;dia;mes;año)	Matriz (lista de listas)
productos.json	Productos	Diccionario (clave: ID del producto)
ventas.json	Ventas acumuladas por producto	Diccionario (clave: tupla con ID y nombre)
usuarios.json	Usuarios del sistema	Lista de diccionarios

Las matrices se guardan en archivos de texto y los diccionarios en archivos JSON. El repositorio incluye datos de prueba (10 registros en cada archivo). Si un archivo no existe, el programa arranca con esa información vacía; en el caso de usuarios.json, lo crea con los usuarios iniciales.

Usuarios de prueba
Usuario	Contraseña	Tipo
admin	1234	Administrador
usuario	1234	Usuario
Tecnologías y conceptos utilizados
Python
Listas, slicing y listas por comprensión
Matrices (listas de listas)
Diccionarios y listas de diccionarios
Tuplas
Conjuntos y operaciones entre conjuntos (unión, intersección y diferencia)
Cadenas: métodos, rebanadas y f-strings
Expresiones regulares
map, filter, reduce y lambda
Recursividad
Manejo de excepciones (try/except)
Archivos de texto: alta en modo append, y baja y modificación con archivo auxiliar
Archivos JSON
Modularización
Git y GitHub
Cambios respecto de la primera entrega

A partir de la devolución de la primera entrega se realizaron las siguientes mejoras:

Los productos y los proveedores se relacionan por ID.

Los patrones de las expresiones regulares aceptan tildes, ñ y ü.

Las búsquedas por proveedor ya no usan el texto ingresado como patrón de expresión regular.

Se agregaron operaciones entre conjuntos: proveedores sin productos, categorías sin ventas y productos vendidos que se quedaron sin stock.

Se agregaron conteos y promedios por categoría y por proveedor, y un resumen estadístico.

Se limitó el inicio de sesión a 3 intentos y se agregó una opción para salir del programa.

Se eliminó main_prueba.py y los imports con asterisco.

El menú quedó separado de la lógica del programa.

Se agregó el guardado de datos en archivos TXT y JSON.

Integrantes

Integrante	Legajo

Iván Ricardo Martínez Sccasso	1223079

Lorenzo Resnik	1215403

Franco Schwab	1238148

Damián Siles	1238437

Scrum Master: Lorenzo Resnik

Recursos
Repositorio: https://github.com/loloresnik/grupo5-progra1

Primera entrega

Video de presentación: https://youtu.be/ZnmKXiAl1yw

Video de funcionamiento: https://youtu.be/UmUBWy5wKCc

Segunda entrega

Video: 

Objetivo

Aplicar los contenidos de Programación 1 mediante el desarrollo de un sistema modular para gestionar el inventario de un local de computación de forma organizada, incorporando validaciones, estructuras de datos, archivos, recursividad, diferentes niveles de acceso y reportes.
