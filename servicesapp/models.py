from django.db import models
from django.urls import reverse

# Create your models here.
class servicespage(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='portfolioapp/images/')
    slug = models.SlugField(null=True) # new

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ServicesDetail', kwargs={'slug': self.slug})
