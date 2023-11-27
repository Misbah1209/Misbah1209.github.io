from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Creating the models for the database here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Tip(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    img = models.ImageField(upload_to='tips_image/',null=True,blank=True)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20,null=False)
    
    def __str__(self):
        return self.user.username

class Season(models.Model):
    name = models.CharField(max_length=128)
    maxtemp = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
    mintemp = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
    
    def __str__(self):
        return self.name

class Outfit(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='outfits_image/',null=True,blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=128, unique=True)
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(List, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title