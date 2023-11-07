from django.forms import ModelForm, forms
from .models import Product, ProductCategory
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'cost': 'Precio',
            'category': "Categoria"
        }

    def clean_cost(self):
        self.cost = self.cleaned_data.get('cost')
        if self.cost <= 0:
            raise forms.ValidationError("El costo de un producto debe ser mayor a 0")
        return self.cost

class ProductCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        labels = {
            'name': 'Cateogria',}

class FactorForm(forms.Form):

    factor = forms.FloatField()

    def clean_factor(self):
        factor = self.cleaned_data.get('factor')
        if factor <= 0:
            raise forms.ValidationError("El factor no puede ser menor o igual a 0")
        return factor