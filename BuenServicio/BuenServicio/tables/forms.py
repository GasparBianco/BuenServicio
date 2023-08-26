from typing import Any, Dict
from django import forms

class OneTableForm(forms.Form):
    number = forms.IntegerField()

class ManyTableForm(forms.Form):
    start = forms.IntegerField()
    end = forms.IntegerField()

    def clean_start(self):
        start = self.cleaned_data.get('start')
        if start < 0:
            raise forms.ValidationError("El valor de inicio debe ser mayor o igual a 0.")
        return start
        
    def clean_end(self):
        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
        if end <= start:
            raise forms.ValidationError("El valor final debe ser mayor que el valor de inicio.")
        return end