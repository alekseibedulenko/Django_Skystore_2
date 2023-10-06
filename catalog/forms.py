from django import forms
from .models import Product, Version


class ProductForm(forms.ModelForm):
    forbidden_words = {'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'}
    version = forms.ModelChoiceField(queryset=Version.objects.all(), required=False, empty_label="Выберите версию")

    class Meta:
        model = Product
        fields = ['name', 'description', 'preview_description', 'image', 'category', 'price', 'version']

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        if set(name.split()).intersection(self.forbidden_words):
            raise forms.ValidationError(f"Нельзя использовать запрещенное слово в названии продукта.")
        return name

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        if set(description.split()).intersection(self.forbidden_words):
            raise forms.ValidationError(f"Нельзя использовать запрещенное слово в описании продукта.")
        return description



