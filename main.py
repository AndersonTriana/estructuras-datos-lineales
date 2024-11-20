from lista_productos import ListaProductos
from clases import Producto

def mostrar_menu():
    print("\n===== Menú de Opciones =====")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Mostrar lista de productos")
    print("5. Calcular precio total de productos")
    print("6. Encontrar producto con precio máximo")
    print("7. Encontrar producto con precio mínimo")
    print("8. Calcular promedio de precios de productos")
    print("9. Salir")
    print("============================")

def main():
    lista = ListaProductos()
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            producto = Producto(nombre, precio, cantidad)
            lista.adicionar_producto(producto)
            print(f"Producto '{nombre}' agregado exitosamente.")
        
        elif opcion == "2":
            nombre = input("Nombre del producto a buscar: ")
            producto = lista.buscar_producto(nombre)
            if producto:
                print(f"Producto encontrado: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")
            else:
                print("Producto no encontrado.")
        
        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            exito = lista.eliminar_producto(nombre)
            if exito:
                print(f"Producto '{nombre}' eliminado exitosamente.")
            else:
                print("Producto no encontrado.")
        
        elif opcion == "4":
            print("\nLista de productos:")
            lista.imprimir_lista()
        
        elif opcion == "5":
            total = lista.calcular_precio_total()
            print(f"El precio total de todos los productos es: {total}")
        
        elif opcion == "6":
            maximo = lista.encontrar_maximo()
            if maximo:
                print(f"Producto más caro: {maximo.nombre}, Precio: {maximo.precio}")
            else:
                print("No hay productos en la lista.")
        
        elif opcion == "7":
            minimo = lista.encontrar_minimo()
            if minimo:
                print(f"Producto más barato: {minimo.nombre}, Precio: {minimo.precio}")
            else:
                print("No hay productos en la lista.")
        
        elif opcion == "8":
            promedio = lista.calcular_promedio_precio()
            if promedio is not None:
                print(f"El precio promedio de los productos es: {promedio:.2f}")
            else:
                print("No hay productos en la lista para calcular el promedio.")
        
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()