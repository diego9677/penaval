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


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nit', 'nombres', 'apellidos']
        widgets = {
            'nit': forms.TextInput(attrs={'placeholder': 'Nit'}),
            'nombres': forms.TextInput(attrs={'placeholder': 'Nombres'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Apellidos'})
        }
