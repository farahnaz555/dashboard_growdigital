from django.db import models
from django.urls import reverse

# Create your models here.
class careerpagepage(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=500)

    image = models.ImageField(upload_to='careerpageapp/images/')
    slug = models.SlugField(null=True) # new


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('CareerPageDetail', kwargs={'slug': self.slug})
