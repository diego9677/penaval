from django.urls import path
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView
)

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto-list'),
    path('crear/', ProductoCreateView.as_view(), name='producto-create'),
    path('editar/<int:pk>/',
         ProductoUpdateView.as_view(), name='producto-update'),
    path('eliminar/<int:pk>/',
         ProductoDeleteView.as_view(), name='producto-delete')
]
