from django.forms import fields, widgets
from superadmin import models
from django import forms
from django.contrib.auth.models import User

class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.servicespage
         fields = ['title','image','description']
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
        }
