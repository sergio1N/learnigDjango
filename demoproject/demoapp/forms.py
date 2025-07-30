from django import forms
from django.forms.widgets import NumberInput

class MiFormulario(forms.Form):
    name=forms.CharField(label='Name', max_length=100)
    email= forms.EmailField(label='Los correos' )
    date=forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label='Datess')
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
    field = forms.ChoiceField(choices=posts) 
    year=forms.IntegerField(label='Year', min_value=2000, max_value=2025)
    img=forms.ImageField(label='Image', required=False)