class CarritoVenta:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito_venta', None)
        if not carrito:
            self.session['carrito_venta'] = {}
            self.carrito = self.session['carrito_venta']
        else:
            self.carrito = carrito

    def agregar(self, producto, cantidad):
        id = str(producto.id)
        self.carrito[id] = {
            'producto_id': producto.id,
            'codigo': producto.codigo,
            'marca': producto.marca.nombre,
            'medidas': producto.medidas,
            'cantidad': cantidad,
            'precio': float(producto.precio_unitario),
            'acumulado': float(cantidad * producto.precio_unitario),
        }
        self.guardar()

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            del self.carrito[id]
            self.guardar()

    def limpiar(self):
        self.session['carrito_venta'] = {}
        self.session.modified = True

    def guardar(self):
        self.session['carrito_venta'] = self.carrito
        self.session.modified = True
