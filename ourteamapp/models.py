from django.db import models
from django.urls import reverse
import random
from django.template.defaultfilters import slugify
from django.conf import settings


# Create your models here.
class ourteampage(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,null=True, unique=True, blank=True)
    designation = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='ourteamapp/images/')
    # slug = models.SlugField(null=True) # new
  
    # def get_absolute_url(self):
    #     kwargs = {
    #         'slug': self.slug
    #     }
    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(ourteampage, self).save(*args, **kwargs)
 
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('OurTeamDetail', kwargs={'slug': self.slug})
