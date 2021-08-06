from django.db import models
from django.urls import reverse


# Create your models here.
class businesspartnerpage(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=500)
    slug = models.SlugField(null=True) # new


    image = models.ImageField(upload_to='businesspartnerapp/images/')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('BusinessPartnerDetail', kwargs={'slug': self.slug})
