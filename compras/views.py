from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.db.models import Q
from compras.carrito import Carrito
from productos.models import Producto
from .models import Proveedor


def compras(request):
    productos = Producto.objects.all()
    return render(request, 'compras/compras.html', {'productos': productos})


class ProveedorListView(ListView):
    model = Proveedor

    def get_queryset(self):
        word = self.request.GET.get('word', '')
        proveedores = Proveedor.objects.filter(
            Q(nombre__icontains=word) | Q(direccion__icontains=word))
        return proveedores


class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = ['nombre', 'direccion']
    success_url = reverse_lazy('proveedor-list')


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = ['nombre', 'direccion']
    success_url = reverse_lazy('proveedor-list')


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedor-list')


def agregar_producto(request, pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=pk)
    carrito.agregar(producto)
    return redirect(reverse_lazy('compras'))


def eliminar_producto(request, pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=pk)
    carrito.eliminar(producto)
    return redirect(reverse_lazy('compras'))


def restar_producto(request, pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=pk)
    carrito.restar(producto)
    return redirect(reverse_lazy('compras'))


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(reverse_lazy('compras'))
