from django import forms

class OneTableForm(forms.Form):
    number = forms.IntegerField()

class ManyTableForm(forms.Form):
    start = forms.IntegerField()
    end = forms.IntegerField()
        
    def clean(self):
        cleaned_data = super().clean()
        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
        if start < 0:
            raise forms.ValidationError("El valor final debe ser mayor que el valor de inicio.")
        elif end <= start:
            raise forms.ValidationError("El valor final debe ser mayor que el valor de inicio.")
        return cleaned_data