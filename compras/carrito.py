class CarritoCompra:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito_compra', None)
        if not carrito:
            self.session['carrito_compra'] = {}
            self.carrito = self.session['carrito_compra']
        else:
            self.carrito = carrito

    def agregar(self, producto, cantidad, precio_compra, precio_venta):
        id = str(producto.id)
        self.carrito[id] = {
            'producto_id': producto.id,
            'codigo': producto.codigo,
            'cantidad': cantidad,
            'precio_compra': float(precio_compra),
            'precio_venta': float(precio_venta),
            'acumulado': float(cantidad * precio_compra),
        }
        self.guardar()

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            del self.carrito[id]
            self.guardar()

    def limpiar(self):
        self.session['carrito_compra'] = {}
        self.session.modified = True

    def guardar(self):
        self.session['carrito_compra'] = self.carrito
        self.session.modified = True
