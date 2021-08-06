from django.db import models
from django.urls import reverse

class customerreviewpage(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    email = models.EmailField(max_length=254, blank=False)
    slug = models.SlugField(null=True) # new



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CustomerReviewDetail', kwargs={'slug': self.slug})
