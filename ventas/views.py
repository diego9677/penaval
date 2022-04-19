from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from productos.models import Producto
from .models import Venta, DetalleVenta
from .forms import ProductoSelectForm, ClienteForm
from .carrito import CarritoVenta


@login_required
def ventas(request):
    word = request.GET.get('word', '')
    form_producto = ProductoSelectForm()
    form_cliente = ClienteForm()
    productos = Producto.objects.filter(
        Q(codigo__icontains=word) | Q(medidas__icontains=word) |
        Q(marca__nombre__icontains=word)).all()
    context = {
        'productos': productos,
        'form_producto': form_producto,
        'form_cliente': form_cliente
    }
    return render(request, 'ventas/ventas.html', context)


@login_required
def agregar_producto(request, pk):
    if request.method == 'POST':
        form = ProductoSelectForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data.get('cantidad', None)
            carrito = CarritoVenta(request)
            producto = Producto.objects.get(pk=pk)
            if cantidad <= producto.cantidad_disponible:
                carrito.agregar(producto, cantidad)
            return redirect(reverse_lazy('ventas'))
    return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])


@login_required
def eliminar_producto(request, pk):
    carrito = CarritoVenta(request)
    producto = Producto.objects.get(pk=pk)
    carrito.eliminar(producto)
    return redirect(reverse_lazy('ventas'))


@login_required
def limpiar_carrito(request):
    carrito = CarritoVenta(request)
    carrito.limpiar()
    return redirect(reverse_lazy('ventas'))


@login_required
def guardar_compra(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.usuario = request.user
            cliente.save()
            carrito = CarritoVenta(request)
            venta = Venta.objects.create(usuario=request.user, cliente=cliente)
            for key, value in carrito.carrito.items():
                producto_id = value.get('producto_id')
                cantidad = value.get('cantidad')
                precio = value.get('precio')
                subtotal = value.get('acumulado')
                DetalleVenta.objects.create(
                    venta=venta,
                    producto_id=producto_id,
                    cantidad=cantidad,
                    precio_unitario=precio,
                    subtotal=subtotal
                )
                producto = Producto.objects.get(pk=producto_id)
                producto.cantidad_disponible -= cantidad
                producto.save()
            carrito.limpiar()
            return redirect(reverse_lazy('ventas'))
    return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])
