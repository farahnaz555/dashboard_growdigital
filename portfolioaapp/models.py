from django.db import models
from django.urls import reverse

# Create your models here.
class portfoliopage(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolioapp/images/')
    slug = models.SlugField(null=True) # new


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PortfolioDetail', kwargs={'slug': self.slug})
