from django.contrib import admin
from .models import Lugar, Marca, Producto


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    pass


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    pass


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass
