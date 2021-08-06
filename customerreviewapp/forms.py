from django.forms import ModelForm
from .models import customerreviewpage

class customerreviewform(ModelForm):
    class Meta:
        model = customerreviewpage
        fields = ['name', 'message', 'email']
