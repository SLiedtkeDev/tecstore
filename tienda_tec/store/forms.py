from django import forms
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import Product, Order


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        total = self.request.session.get('total')
        # total = 200
        initial = kwargs.get('initial', {})
        initial['total'] = total

        super().__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = ['email', 'name', 'address', 'neighborhood', 'total']

        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'neighborhood': TextInput(attrs={'class': 'form-control', 'placeholder': 'Colonia'}),
            'total': TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
