from dal import autocomplete
from django import forms

from vkapp.models import ProductSales, Sales


class ProductSalesAdminForm(forms.ModelForm):
    class Meta:
        model = ProductSales
        fields = ('__all__')
        widgets = {
                'product': autocomplete.ModelSelect2(url='product-autocomplete', attrs={
                'data-placeholder': 'Enter model name or model number...',
                'data-minimum-input-length': 3,
                },)
        }

class SalesAdminForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ('__all__')
        widgets = {
                'customer': autocomplete.ModelSelect2(url='customer-autocomplete', attrs={
                'data-placeholder': 'Enter name or mobile number...',
                'data-minimum-input-length': 3,
                },)
        }