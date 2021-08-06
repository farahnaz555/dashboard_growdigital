from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, EmailField
from django.template.defaultfilters import slugify, truncatechars
from django.urls import resolve
import uuid
import random
from django.urls import reverse


class consultationpage(models.Model):
    title = models.CharField(max_length=200 ,null= True)
    name = models.CharField(max_length=100)
    message = models.TextField(blank=False)
    email = models.EmailField(max_length=254, blank=False)
    contact = models.IntegerField(blank=False)
    service = models.TextField(max_length=254, blank=False)
    #service = models.ForeignKey(servicespage , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

# Create your models here.
class homepage(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    slug = models.SlugField(null=True) # new


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('HomeDetail', kwargs={'slug': self.slug})

class businesspartnerpage(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=500)
    slug = models.SlugField(null=True) # new
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class ourclient(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    email = models.EmailField(max_length=254, blank=False)
    contact = models.IntegerField(blank=False)
    slug = models.SlugField(null=True) # new
    image = models.ImageField(upload_to='static/images/')
    created_at = models.DateTimeField(auto_now=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
   

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class customerreviewpage(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    email = models.EmailField(max_length=254, blank=False)
    
    slug = models.SlugField(null=True) # new



    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=200)
   # category = models.CharField(max_length=200)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='static/images/')
    created_at = models.DateTimeField(auto_now=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class servicespage(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='static/images/')
    slug = models.SlugField(null=True) # new

    def __str__(self):
        return self.title

    

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class portfoliopage(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='static/images/')
    slug = models.SlugField(null=True) # new

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class careerpagepage(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=500)

    image = models.ImageField(upload_to='static/images/')
    slug = models.SlugField(null=True) # new


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class ContactModel(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    # image = models.ImageField(upload_to ="static/Contact/")
    short_description = models.CharField(max_length=500)
    message = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class priceandpackagesmodel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,null=True, unique=True, blank=True)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100 ,null=True)
    quantity_purchased = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    #slug = models.SlugField(null=True) # new

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(priceandpackagesmodel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ourteampage(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,null=True, unique=True, blank=True)
    designation = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='static/images/')
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
class aboutuspage(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    slug = models.SlugField(null=True)



    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class termsncpage(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    slug = models.SlugField(null=True) # new

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('TermsAndConditionDetail', kwargs={'slug': self.slug})

class privacypolicypage(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    slug = models.SlugField(null=True) # new

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PrivacyPolicyDetail', kwargs={'slug': self.slug})


class sitemappage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sitemap/images/')
    slug = models.SlugField(null=True) # new


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('SiteMapDetail', kwargs={'slug': self.slug})
