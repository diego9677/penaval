from django.contrib import admin
from .models import Venta, DetalleVenta


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'usuario', 'cliente', 'fecha_emision')


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'producto', 'cantidad',
                    'precio_unitario', 'subtotal')
