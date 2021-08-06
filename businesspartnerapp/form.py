from django.forms import fields, widgets
from superadmin import models
from django import forms
from django.contrib.auth.models import User

class BusinessForm(forms.ModelForm):
    class Meta:
        model = models.businesspartnerpage
        fields = ['title','image','short_description','long_description']
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
        }