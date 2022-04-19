from django import forms
from .models import Cliente


class ProductoSelectForm(forms.Form):
    cantidad = forms.IntegerField(
        required=True,
        min_value=0,
        label='Cantidad',
        widget=forms.NumberInput(
            attrs={'placeholder': 'Cantidad'}
        )
    )


class ClienteForm(forms.Form):
    nit = forms.CharField(
        max_length=20,
        label='Nit',
        widget=forms.TextInput(
            attrs={'placeholder': 'Nit'}
        )
    )
    nombres = forms.CharField(
        max_length=255,
        label='Nombres',
        widget=forms.TextInput(
            attrs={'placeholder': 'Nombres'}
        )
    )
    apellidos = forms.CharField(
        max_length=255,
        label='Apellidos',
        widget=forms.TextInput(
            attrs={'placeholder': 'Apellidos'}
        )
    )
