from django.contrib import admin
from .models import Venta, DetalleVenta


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    pass


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    pass
