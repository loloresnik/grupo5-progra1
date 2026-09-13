import re

def agregar_proveedor(proveedores, proveedor):
    #Agrega un nuevo proveedor a la matriz
    proveedores.append(proveedor)
    return proveedores

def buscar_proveedor(proveedores, nombre):
    #Busca un proveedor en la matriz por su nombre
    #Retorna una lista de filas con las coincidencias con el nombre
    resultado = []
    for fila in proveedores:
        if fila[1].lower() == nombre.lower():
            resultado.append(fila)
    return resultado


def modificar_proveedor(proveedores, nombre, nuevo_nombre, nuevo_telefono, nuevo_mail):
    #Modifica los datos de un proveedor en la matriz introduciendo su nombre
    for proveedor in proveedores:
        if proveedor[1].lower() == nombre.lower():
            proveedor[1] = nuevo_nombre
            proveedor[2] = nuevo_telefono
            proveedor[3] = nuevo_mail
    return proveedores


def eliminar_proveedor(proveedores, nombre):
    #Elimina un proveedor de la matriz introduciendo su npmbre
    nuevos_proveedores = []
    for fila in proveedores:
        if fila[1].lower() != nombre.lower():
            nuevos_proveedores.append(fila)
    proveedores[:] = nuevos_proveedores
    return proveedores


def mostrar_proveedores(proveedores):
    #Muestra la matriz completa de proveedores
    return proveedores


def buscar_productos_por_proveedor(inventario, proveedor):
    # Busca los productos que pertenecen al proveedor asignado
    resultado = []
    for fila in inventario:
        if re.search(proveedor, fila[4], re.IGNORECASE):
            resultado.append(fila)
    return resultado

def stock_por_proveedor(inventario, proveedor):
    # Suma el stock de los productos del proveedor
    total = 0

    for fila in inventario:
        if re.search(proveedor, fila[4], re.IGNORECASE):
            total += fila[3]

    return total

