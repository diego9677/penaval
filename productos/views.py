from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Producto
from .forms import ProductoForm


class ProductoListView(LoginRequiredMixin, ListView):
    # login required mixin
    login_url = reverse_lazy('login')
    # list view
    model = Producto

    def get_queryset(self):
        word = self.request.GET.get('word', '')
        productos = Producto.objects.filter(
            Q(codigo__icontains=word) | Q(medidas__icontains=word) |
            Q(marca__nombre__icontains=word)).all()
        return productos


class ProductoCreateView(LoginRequiredMixin, CreateView):
    # login required mixin
    login_url = reverse_lazy('login')
    # Create View section
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto-list')


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    # login required mixin
    login_url = reverse_lazy('login')
    # view saection
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto-list')


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    # login required mixin
    login_url = reverse_lazy('login')
    # view section
    model = Producto
    success_url = reverse_lazy('producto-list')
