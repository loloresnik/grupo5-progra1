import re

def agregar_proveedor(proveedores, proveedor):
    """
    proveedor = [id, nombre, telefono, mail]
    """
    proveedores.append(proveedor)
    return proveedores


def buscar_proveedor(proveedores, nombre):
    resultado = []
    for fila in proveedores:
        if fila[1].lower() == nombre.lower():
            resultado.append(fila)
    return resultado


def modificar_proveedor(proveedores, nombre, nuevo_nombre, nuevo_telefono, nuevo_mail, productos_dic):
    """
    Modifica proveedor en la matriz y también en los productos.
    """

    # Modificar en matriz
    for fila in proveedores:
        if fila[1].lower() == nombre.lower():
            fila[1] = nuevo_nombre
            fila[2] = nuevo_telefono
            fila[3] = nuevo_mail

    # Modificar en productos
    for p in productos_dic:
        if p["proveedor"].lower() == nombre.lower():
            p["proveedor"] = nuevo_nombre

    return proveedores


def eliminar_proveedor(proveedores, nombre, productos_dic):
    """
    Solo elimina si NO hay productos asociados.
    """

    # Verificar si el proveedor tiene productos
    for p in productos_dic:
        if p["proveedor"].lower() == nombre.lower():
            print("No se puede eliminar: el proveedor tiene productos asociados.")
            return proveedores

    nuevos = []
    for fila in proveedores:
        if fila[1].lower() != nombre.lower():
            nuevos.append(fila)

    proveedores[:] = nuevos
    return proveedores


def buscar_productos_por_proveedor(productos_dic, proveedor):
    resultado = []

    for p in productos_dic:
        if re.search(proveedor, p["proveedor"], re.IGNORECASE):
            resultado.append(p)

    return resultado

def stock_por_proveedor(productos_dic, proveedor):
    total = 0

    for p in productos_dic:
        if re.search(proveedor, p["proveedor"], re.IGNORECASE):
            total += p["stock"]

    return total