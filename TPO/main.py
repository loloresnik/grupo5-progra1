import gestion_productos
from functools import reduce

def main():
    productos = []
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

            gestion_productos.agregar_producto(productos)

        
        elif opcion == 2:

            gestion_productos.mostrar_productos(productos)

        
        elif opcion == 3:

            productos.sort(key=lambda p: p[1])
            print("Productos ordenados por nombre:")

            print("#" * 80)
            print("Producto        Categoria       Proveedor        Stock")
            print("#" * 80)
            
            for fila in productos:
                print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:>5}")
            
            print("#" * 80)

        # 4. Ordenar por stock
        elif opcion == 4:

            ordenados = sorted(productos, key=lambda p: p[4])
            print("Productos ordenados por stock:")

            print("#" * 80)
            print("ID             Nombre          Categoria       Proveedor       Stock")
            print("#" * 80)

            for fila in ordenados:

                print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:>5}")

            print("#" * 80)

        # 5. Filtrar stock bajo
        elif opcion == 5:

            limite = int(input("Ingrese límite de stock: "))
            bajos = list(filter(lambda p: p[4] < limite, productos))

            print("Productos con stock menor al límite:")

            print("#" * 80)
            print("ID             Nombre          Categoria       Proveedor       Stock")
            print("#" * 80)

            for fila in bajos:

                print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:>5}")

            print("#" * 80)


        # 6. Obtener nombres
        elif opcion == 6:

            nombres = list(map(lambda p: p[1], productos))

            print("Nombres de productos:")

            print("#" * 40)
            print("Nombre")
            print("#" * 40)

            for nombre in nombres:
                print(f"{nombre:<30}")

            print("#" * 40)
           
        # 7. Stock total
        elif opcion == 7:
            total = reduce(lambda acum, p: acum + p[4], productos, 0)

            print("#" * 40)
            print(f"{'Stock total en inventario:':<30} {total:>5}")
            print("#" * 40)

        elif opcion == 0:

            print("Saliendo del sistema...")
            seguir = 0

        else:
            print("Opción inválida.")

main()