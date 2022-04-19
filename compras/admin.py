from django.contrib import admin
from .models import Proveedor, Compra, DetalleCompra


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nombre', 'direccion')


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('pk', 'usuario', 'proveedor', 'fecha_emision')


@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ('pk', 'producto', 'cantidad',
                    'precio_unitario_compra', 'precio_unitario_venta')
