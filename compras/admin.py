from django.contrib import admin
from .models import Proveedor, Compra, DetalleCompra


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    pass


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    pass


@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    pass
