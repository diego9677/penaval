from django.contrib import admin
from .models import Lugar, Marca, Producto


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nombre', 'descripcion')


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nombre', 'descripcion')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'codigo', 'lugar', 'marca', 'medidas',
                    'cantidad_disponible', 'precio_unitario')
