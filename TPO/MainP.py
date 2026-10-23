import menu
import archivos


def main():
    # Toda la información se recupera desde los archivos de la carpeta "datos"
    datos = archivos.cargar_datos()

    while True:
        print("\n==============================")
        print("    GESTION DE INVENTARIO")
        print("==============================")
        print("1. Iniciar sesion")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            sesion = menu.iniciar_sesion(datos["usuarios"])

            if sesion is not None:
                usuario, rol = sesion
                menu.menu_principal(datos, rol)

        elif opcion == "0":
            archivos.guardar_datos(datos)
            print("Datos guardados. Hasta luego.")
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
