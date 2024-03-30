from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super(StyleFormMixin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_name', 'product_about', 'product_price', 'product_category', 'image', 'is_published')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

        for word in words:
            if word[:-1] in cleaned_data.lower():
                raise forms.ValidationError('Название содержит запрещенное слово')

        return cleaned_data

    def clean_product_about(self):
        cleaned_data = self.cleaned_data['product_about']
        words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

        for word in words:
            if word[:-1] in cleaned_data.lower():
                raise forms.ValidationError('Описание содержит запрещенное слово')

        return cleaned_data


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_about', 'product_category', 'is_published')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

        for word in words:
            if word[:-1] in cleaned_data.lower():
                raise forms.ValidationError('Название содержит запрещенное слово')

        return cleaned_data

    def clean_product_about(self):
        cleaned_data = self.cleaned_data['product_about']
        words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

        for word in words:
            if word[:-1] in cleaned_data.lower():
                raise forms.ValidationError('Описание содержит запрещенное слово')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
