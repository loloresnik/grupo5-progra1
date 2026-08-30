import gestion_productos
from functools import reduce

def main():

    seguir = 1

    while seguir == 1:

        print("\n===== MENÚ DE PRODUCTOS =====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Ordenar productos por nombre (lambda + sort)")
        print("4. Ordenar productos por stock (lambda + sorted)")
        print("5. Ver productos con stock bajo (lambda + filter)")
        print("6. Ver solo los nombres de productos (lambda + map)")
        print("7. Ver stock total (lambda + reduce)")
        print("0. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            gestion_productos.agregar_producto()

        
        elif opcion == 2:
            gestion_productos.mostrar_productos()

        
        elif opcion == 3:
            gestion_productos.productos.sort(key=lambda p: p[1])
            print("Productos ordenados por nombre:")
            gestion_productos.mostrar_productos()

        # 4. Ordenar por stock
        elif opcion == 4:
            ordenados = sorted(gestion_productos.productos, key=lambda p: p[4])
            print("Productos ordenados por stock:")
            for p in ordenados:
                print(p)

        # 5. Filtrar stock bajo
        elif opcion == 5:
            limite = int(input("Ingrese límite de stock: "))
            bajos = list(filter(lambda p: p[4] < limite, gestion_productos.productos))
            print("Productos con stock menor al límite:")
            for p in bajos:
                print(p)

        # 6. Obtener nombres
        elif opcion == 6:
            nombres = list(map(lambda p: p[1], gestion_productos.productos))
            print("Nombres de productos:")
            print(nombres)

        # 7. Stock total
        elif opcion == 7:
            total = reduce(lambda acum, p: acum + p[4], gestion_productos.productos, 0)
            print("Stock total en inventario:", total)

        # 0. Salir
        elif opcion == 0:
            print("Saliendo del sistema...")
            seguir = 0

        else:
            print("Opción inválida.")

main()