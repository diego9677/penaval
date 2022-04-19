from django.urls import path
from .views import (
    ventas,
    agregar_producto,
    eliminar_producto,
    limpiar_carrito,
    guardar_venta_or_proforma,
    ProformaPdfView
)

urlpatterns = [
    path('agregar/producto/<int:pk>/', agregar_producto, name='ventas-add-producto'),
    path('eliminar/producto/<int:pk>/', eliminar_producto, name='ventas-del-producto'),
    path('ver/proforma/<int:pk>/', ProformaPdfView.as_view(), name='ver-proforma'),
    path('limpiar/carrito/', limpiar_carrito, name='ventas-clean'),
    path('guardar/venta/', guardar_venta_or_proforma, name='ventas-or-proforma-save'),
    path('', ventas, name='ventas'),
]
