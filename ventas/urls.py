from django.urls import path
from .views import (
    ventas,
    agregar_producto,
    eliminar_producto,
    limpiar_carrito,
    guardar_compra
)

urlpatterns = [
    path("agregar/producto/<int:pk>/",
         agregar_producto, name="ventas-add-producto"),
    path("eliminar/producto/<int:pk>/",
         eliminar_producto, name="ventas-del-producto"),
    path("limpiar/carrito/", limpiar_carrito, name="ventas-clean"),
    path("guardar/venta/", guardar_compra, name="ventas-save"),
    path('', ventas, name='ventas')
]
