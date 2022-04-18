from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'lugar', 'marca', 'medidas']
        labels = {
            'codigo': 'Código',
            'marca': 'Marca',
            'lugar': 'Ubicaión',
            'medidas': 'Medidas'
        }
