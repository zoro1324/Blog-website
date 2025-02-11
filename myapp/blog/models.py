from django.db import models
from django.utils.text import slugify
# Create your models here.

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.catagory_name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=3000)
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.slug
    

class AboutUs(models.Model):
    content = models.TextField()
    image = models.URLField()