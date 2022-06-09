from django import forms

class ProjectForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    type = forms.CharField(max_length=40, label='Apellido')

