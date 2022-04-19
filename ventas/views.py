import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.http import HttpResponseNotAllowed, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import View
from weasyprint import HTML, CSS

from productos.models import Producto
from registration.models import Cliente
from .models import Venta, DetalleVenta, Proforma, DetalleProforma
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
def guardar_venta_or_proforma(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        click_guardar_proforma = request.POST.get('guardar_proforma', None)
        click_guarder_venta = request.POST.get('guardar_venta', None)
        if form.is_valid():
            nit = form.cleaned_data.get('nit', None)
            cliente, created = Cliente.objects.get_or_create(nit=nit, defaults={**form.cleaned_data})
            carrito = CarritoVenta(request)

            if click_guarder_venta:
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

            if click_guardar_proforma:
                proforma = Proforma.objects.create(usuario=request.user, cliente=cliente)
                for key, value in carrito.carrito.items():
                    producto_id = value.get('producto_id')
                    cantidad = value.get('cantidad')
                    precio = value.get('precio')
                    subtotal = value.get('acumulado')
                    DetalleProforma.objects.create(
                        proforma=proforma,
                        producto_id=producto_id,
                        cantidad=cantidad,
                        precio_unitario=precio,
                        subtotal=subtotal
                    )
                carrito.limpiar()
                return redirect(reverse_lazy('ver-proforma', kwargs={'pk': proforma.pk}))

            return redirect(reverse_lazy('ventas'))
        return redirect(reverse_lazy('ventas'))
    return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])


class ProformaPdfView(View):

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('ventas/proforma.html')
            proforma = Proforma.objects.get(pk=self.kwargs.get('pk'))
            total = 0
            for detalle in proforma.detalle_proforma.all():
                total += detalle.subtotal
            context = {
                'proforma': proforma,
                'total': total
            }
            html = template.render(context)
            bootstrap_url = os.path.join(settings.BASE_DIR, 'core/static/core/bootstrap-5.1.3/css/bootstrap.min.css')
            css_url = os.path.join(settings.BASE_DIR, 'core/static/core/index.css')
            pdf = HTML(string=html).write_pdf(stylesheets=[CSS(bootstrap_url), CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('ventas'))
