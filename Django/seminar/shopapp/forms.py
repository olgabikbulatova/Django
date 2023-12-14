from django import forms
from django.forms import ModelForm
from .models import Product


class ProdEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'image')
    # ed_prod = Product.objects.get()
    # name = forms.ModelChoiceField(label='name', queryset=ed_prod)
    # description = forms.ModelChoiceField(label='description', queryset=ed_prod)
    # price = forms.ModelChoiceField(label='price', queryset=ed_prod)
    # quantity = forms.ModelChoiceField(label='quantity', queryset=ed_prod)
