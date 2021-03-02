from django.forms import ModelForm,TextInput
from django import forms
from .models import Vehicle


class VehicleForm(ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'is_active': forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'plate': TextInput(attrs={'class':'form-control'}),
            'model': TextInput(attrs={'class':'form-control'}),
            'brand': TextInput(attrs={'class':'form-control'}),
            'details': forms.Textarea(attrs={'class':'form-control', 'rows': 2}),
            'driver': forms.Select(attrs={'class':'form-control'}),
        }  