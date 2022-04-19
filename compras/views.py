from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from compras.carrito import CarritoCompra
from productos.models import Producto
from .models import Proveedor, DetalleCompra
from .forms import ProductoSelectForm, CompraForm


@login_required
def compras(request):
    form_producto = ProductoSelectForm()
    form_compra = CompraForm()
    word = request.GET.get('word', '')
    productos = Producto.objects.filter(
        Q(codigo__icontains=word) | Q(medidas__icontains=word) |
        Q(marca__nombre__icontains=word)).all()
    context = {
        'productos': productos,
        'form_producto': form_producto,
        'form_compra': form_compra
    }
    return render(request, 'compras/compras.html', context)


class ProveedorListView(LoginRequiredMixin, ListView):
    # login required mixin
    login_url = reverse_lazy('login')
    # ListView section
    model = Proveedor

    def get_queryset(self):
        word = self.request.GET.get('word', '')
        proveedores = Proveedor.objects.filter(
            Q(nombre__icontains=word) | Q(direccion__icontains=word))
        return proveedores


class ProveedorCreateView(LoginRequiredMixin, CreateView):
    # login required mixin
    login_url = reverse_lazy('login')
    # view section
    model = Proveedor
    fields = ['nombre', 'direccion']
    success_url = reverse_lazy('proveedor-list')


class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
    # login required mixin
    login_url = reverse_lazy('login')
    # view section
    model = Proveedor
    fields = ['nombre', 'direccion']
    success_url = reverse_lazy('proveedor-list')


class ProveedorDeleteView(LoginRequiredMixin, DeleteView):
    # login required mixin
    login_url = reverse_lazy('login')
    # view section
    model = Proveedor
    success_url = reverse_lazy('proveedor-list')


@login_required
def agregar_producto(request, pk):
    if request.method == 'POST':
        form = ProductoSelectForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data.get('cantidad', None)
            precio_compra = form.cleaned_data.get('precio_compra', None)
            precio_venta = form.cleaned_data.get('precio_venta', None)
            carrito = CarritoCompra(request)
            producto = Producto.objects.get(pk=pk)
            carrito.agregar(producto, cantidad, precio_compra, precio_venta)
            return redirect(reverse_lazy('compras'))
    return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])


@login_required
def eliminar_producto(request, pk):
    carrito = CarritoCompra(request)
    producto = Producto.objects.get(pk=pk)
    carrito.eliminar(producto)
    return redirect(reverse_lazy('compras'))


@login_required
def limpiar_carrito(request):
    carrito = CarritoCompra(request)
    carrito.limpiar()
    return redirect(reverse_lazy('compras'))


@login_required
def guardar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.usuario = request.user
            compra.save()
            carrito = CarritoCompra(request)
            for key, value in carrito.carrito.items():
                producto_id = value.get('producto_id')
                cantidad = value.get('cantidad')
                precio_compra = value.get('precio_compra')
                precio_venta = value.get('precio_venta')
                DetalleCompra.objects.create(
                    compra=compra,
                    producto_id=producto_id,
                    cantidad=cantidad,
                    precio_unitario_compra=precio_compra,
                    precio_unitario_venta=precio_venta
                )
                producto = Producto.objects.get(pk=producto_id)
                producto.cantidad_disponible += cantidad
                producto.precio_unitario = precio_venta
                producto.save()
            carrito.limpiar()
            return redirect(reverse_lazy('compras'))
    return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])
