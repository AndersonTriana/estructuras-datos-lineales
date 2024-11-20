class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class ProductoDefectuoso(Producto):
    def __init__(self, nombre, precio, cantidad, descripcion_falla):
        super().__init__(nombre, precio, cantidad)
        self.descripcion_falla = descripcion_falla

class NodoProducto:
    def __init__(self, producto, siguiente=None):
        self.producto = producto
        self.siguiente = siguiente
