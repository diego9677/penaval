from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Producto
from .forms import ProductoForm


class ProductoListView(ListView):
    model = Producto

    def get_queryset(self):
        word = self.request.GET.get('word', '')
        productos = Producto.objects.filter(
            Q(codigo__icontains=word) | Q(medidas__icontains=word) |
            Q(marca__nombre__icontains=word)).all()
        return productos


class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto-list')


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto-list')


class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto-list')
