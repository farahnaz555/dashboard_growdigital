from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=500)

    image = models.ImageField(upload_to='blog/images/')
    created_at = models.DateTimeField(auto_now=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(null=True) # new

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('BlogDetailView', kwargs={'slug': self.slug})
            
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)
        