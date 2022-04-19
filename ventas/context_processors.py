def total_carrito_venta(request):
    total = 0
    if request.user.is_authenticated:
        carrito = request.session.get('carrito_venta', None)
        if carrito:
            for key, value in carrito.items():
                total += float(value['acumulado'])
    return {'total_carrito_venta': total}
