from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.catagory_name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=3000)
    image = models.ImageField(null=True,upload_to="post/images")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,max_length=300)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    is_published = models.BooleanField(default=False)

    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def formeted_image(self):

        if self.image.__str__().startswith(('http://','https://')):
            url = self.image
        else:
            url = self.image.url
            
        return url

    def __str__(self):
        return self.slug
    

class AboutUs(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to="blog/aboutus")

    @property
    def formeted_image(self):
        if self.image.__str__().startswith(('http','https')):
            image = self.image
            
        else:
            image = self.image.url
            print(self.image)
        return image

class Contact(models.Model):
    name = models.CharField(max_length=30,null=False)
    email = models.EmailField(null=False)
    message = models.TextField(null=False)