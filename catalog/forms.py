from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_name', 'product_about', 'product_price', 'product_category', 'image',)

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