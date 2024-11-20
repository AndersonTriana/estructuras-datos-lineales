from clases import NodoProducto

class ListaProductos:
    
    def __init__(self):
        self.head = None
        self.cantidad_elementos = 0

    def adicionar_producto(self, producto):
        nodo_nuevo = NodoProducto(producto)

        if self.head is None:
            self.head = nodo_nuevo
            self.cantidad_elementos = 1
        else:
            actual = self.head
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodo_nuevo
            self.cantidad_elementos += 1

    def buscar_producto(self, nombre):
        actual = self.head
        while actual is not None:
            if actual.producto.nombre == nombre:
                return actual.producto
            actual = actual.siguiente
        return None

    def eliminar_producto(self, nombre):
        if self.head is None:
            return False

        if self.head.producto.nombre == nombre:
            self.head = self.head.siguiente
            self.cantidad_elementos -= 1
            return True

        actual = self.head
        while actual.siguiente is not None:
            if actual.siguiente.producto.nombre == nombre:
                actual.siguiente = actual.siguiente.siguiente
                self.cantidad_elementos -= 1
                return True
            actual = actual.siguiente

        return False

    def imprimir_lista(self):
        actual = self.head
        elementos = []
        while actual is not None:
            producto = actual.producto
            elementos.append(f"{producto.nombre} (Precio: {producto.precio}, Cantidad: {producto.cantidad})")
            actual = actual.siguiente
        print(" -> ".join(elementos))

    def calcular_precio_total(self):
        actual = self.head
        precio_total = 0
        while actual is not None:
            producto = actual.producto
            precio_total += producto.precio * producto.cantidad
            actual = actual.siguiente
        return precio_total

    def encontrar_maximo(self):
        
        if self.head is None:
            return None

        maximo = self.head.producto
        actual = self.head.siguiente
        while actual is not None:
            if actual.producto.precio > maximo.precio:
                maximo = actual.producto
            actual = actual.siguiente
        return maximo

    def encontrar_minimo(self):
        if self.head is None:
            return None

        minimo = self.head.producto
        actual = self.head.siguiente
        while actual is not None:
            if actual.producto.precio < minimo.precio:
                minimo = actual.producto
            actual = actual.siguiente
        return minimo

    def calcular_promedio_precio(self):
        if self.cantidad_elementos == 0:
            return None

        precio_total = self.calcular_precio_total()
        promedio = precio_total / self.cantidad_elementos
        return promedio
