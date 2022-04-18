

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito', None)
        if not carrito:
            self.session['carrito'] = {}
            self.carrito = self.session['carrito']
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                'producto_id': producto.id,
                'codigo': producto.codigo,
                'acumulado': float(producto.precio_unitario),
                'cantidad': 1
            }
        else:
            self.carrito[id]['cantidad'] += 1
            self.carrito[id]['acumulado'] += float(producto.precio_unitario)
        self.guardar()

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            del self.carrito[id]
            self.guardar()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]['cantidad'] -= 1
            self.carrito[id]['acumulado'] -= float(producto.precio_unitario)
            if self.carrito[id]['cantidad'] <= 0:
                self.eliminar(producto)
            self.guardar()

    def limpiar(self):
        self.session['carrito'] = {}
        self.session.modified = True

    def guardar(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True
