from django.forms import fields, widgets
from superadmin import models
from django import forms
from django.contrib.auth.models import User


class OurTeam(forms.ModelForm):
    class Meta:
        fields = ['title','designation','image','description']
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
        }

