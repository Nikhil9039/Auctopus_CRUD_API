from django.core import validators
from django import forms
from .models import Product

class ProductRegistration(forms.ModelForm):
 class Meta:
  model = Product
  fields = ['tittle', 'warnty', 'price', 'desc']
  widgets = {
   'tittle': forms.TextInput(attrs={'class':'form-control'}),
   'warnty': forms.NumberInput(attrs={'class':'form-control'}),
   'price': forms.NumberInput(attrs={'class':'form-control'}),
   'desc': forms.TextInput(attrs={'class':'form-control'}),
  }