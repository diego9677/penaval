from django import forms
from .models import Compra


class ProductoSelectForm(forms.Form):
    cantidad = forms.IntegerField(
        required=True,
        min_value=0,
        label='Cantidad',
        widget=forms.NumberInput(
            attrs={'placeholder': 'Cantidad'}
        )
    )
    precio_compra = forms.DecimalField(
        required=True,
        max_digits=9,
        min_value=0,
        decimal_places=2,
        label='Precio Compra',
        widget=forms.NumberInput(
            attrs={'placeholder': 'P. Compra'}
        )
    )
    precio_venta = forms.DecimalField(
        required=True,
        max_digits=9,
        min_value=0,
        decimal_places=2,
        label='Precio Venta',
        widget=forms.NumberInput(
            attrs={'placeholder': 'P. Venta'}
        )
    )


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor']
