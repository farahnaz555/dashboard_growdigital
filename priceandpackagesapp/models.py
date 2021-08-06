from django.db import models
from django.urls import reverse
import random
from django.template.defaultfilters import slugify

# Create your models here.
class priceandpackagesmodel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,null=True, unique=True, blank=True)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    quantity_purchased = models.IntegerField()

    # slug = models.SlugField(null=True) # new

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(priceandpackagesmodel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('PriceAndPackagesDetail', kwargs={'slug': self.slug})
