from cProfile import label
from django import forms
from ARTYapp.models import Profile, Project, Stock, Atelier


class Profile_form(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Name')
    last_name = forms.CharField(max_length=40, min_length=3, label='Last name')
    artist_name = forms.CharField(max_length=20, min_length=1, label='Artist Name')
  #  art_fields = forms.TextField (label = 'Art Fields')
    country = forms.CharField(max_length=16, min_length=4, label='Country')
    email = forms.EmailField(label='Email')

class Project_form(forms.Form):
    project_name = forms.CharField(max_length=40, label='Project')
    project_type = forms.CharField(max_length=40, min_length=4, label='Style')
    #description = forms.TextField()
    add_date = forms.DateField(label='Created on')

class Stock_form(forms.Form):
    Art_piece = forms.CharField(max_length=40, min_length=3, label='Art piece')
    Art_type = forms.CharField(max_length=40, min_length=4, label='Style')
#    description = forms.TextField()
    price = forms.IntegerField(label='$')
    available = forms.BooleanField(label='Stock')

class Atelier_form(forms.Form):
    atelier = forms.CharField(max_length=40, label='Atelier/Artist')
    adress = forms.CharField(max_length=80, label='Adress')