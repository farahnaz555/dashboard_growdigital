from django.forms import ModelForm
from .models import consultationpage

class consultationform(ModelForm):
    class Meta:
        model = consultationpage
        fields = ['name','contact', 'message', 'email']
