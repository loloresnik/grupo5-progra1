import menu
import empleados
import gestion_productos
import proveedores
import Reporte

def main():

    productos_dic = gestion_productos.cargar_productos_json()
    movimientos = gestion_productos.cargar_movimientos_txt()
    ventas_dic = Reporte.cargar_ventas_json()
    proveedores_lista = proveedores.cargar_proveedores_txt()
    usuarios = empleados.cargar_usuarios_json()

    ids_unicos = set(productos_dic.keys())

    opcion = menu.menu_inicio()

    while opcion != "0":

        tipo = empleados.iniciar_sesion(usuarios)

        if tipo == "admin":
            menu.menu_admin(
                usuarios,
                productos_dic,
                movimientos,
                ventas_dic,
                proveedores_lista,
                ids_unicos
            )

        elif tipo == "usuario":
            menu.menu_usuario(
                productos_dic,
                movimientos,
                ventas_dic,
                proveedores_lista,
                ids_unicos
            )

        else:
            print("No se pudo iniciar sesion.")
            break

        opcion = menu.menu_inicio()

    print("Fin del programa.")

if __name__ == "__main__":
    main()
