from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_name', 'product_about', 'product_price', 'product_category')
