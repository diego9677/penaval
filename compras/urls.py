from django.urls import path
from .views import (
    compras,
    agregar_producto,
    restar_producto,
    eliminar_producto,
    limpiar_carrito,
    ProveedorListView,
    ProveedorCreateView,
    ProveedorUpdateView,
    ProveedorDeleteView
)

urlpatterns = [
    path('proveedores/', ProveedorListView.as_view(), name='proveedor-list'),
    path('proveedores/crear/', ProveedorCreateView.as_view(),
         name='proveedor-create'),
    path('proveedores/editar/<int:pk>/',
         ProveedorUpdateView.as_view(), name='proveedor-update'),
    path('proveedores/eliminar/<int:pk>/',
         ProveedorDeleteView.as_view(), name='proveedor-delete'),
    path('agregar/producto/<int:pk>', agregar_producto,
         name='compras-add-producto'),
    path('restar/producto/<int:pk>', restar_producto,
         name='compras-sub-producto'),
    path('eliminar/producto/<int:pk>',
         eliminar_producto, name='compras-del-producto'),
    path('limpiar/carrito/', limpiar_carrito, name='compras-clean'),
    path('', compras, name='compras')
]
