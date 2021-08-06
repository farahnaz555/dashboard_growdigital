from django.db import models
from django.forms import ModelForm
from servicesapp.models import servicespage
from django.urls import reverse



class consultationpage(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=False)
    email = models.EmailField(max_length=254, blank=False)
    contact = models.IntegerField(blank=False)
    service = models.ForeignKey(servicespage , on_delete=models.CASCADE)
    slug = models.SlugField(null=True) # new

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ConsultionDetail', kwargs={'slug': self.slug})
