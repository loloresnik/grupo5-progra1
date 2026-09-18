import menu

def main():
    
    productos_dic = []
    movimientos = []
    ventas_dic = {}
    proveedores_lista = []

    ids_unicos = set()
    categorias_unicas = set()
    proveedores_unicos = set()

    usuarios = [
        {"usuario": "admin", "clave": "1234", "tipo": "admin"},
        {"usuario": "usuario", "clave": "1234", "tipo": "usuario"}
    ]

    while True:
        print("\n==============================")
        print("    GESTION DE INVENTARIO")
        print("==============================")

        tipo = menu.iniciar_sesion(usuarios)

        if tipo == "admin":
            menu.menu_admin(
                usuarios,
                productos_dic,
                movimientos,
                ventas_dic,
                proveedores_lista,
                ids_unicos,
                categorias_unicas,
                proveedores_unicos
            )

        elif tipo == "usuario":
            menu.menu_usuario(
                productos_dic,
                movimientos,
                ventas_dic,
                proveedores_lista,
                ids_unicos,
                categorias_unicas,
                proveedores_unicos
            )

        else:
            print("No se pudo iniciar sesion.")

if __name__ == "__main__":
    main()
