import email
from tabnanny import verbose
from unicodedata import category
from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(Category, related_name='comments', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=50)
    image = models.ImageField(blank=False, upload_to='portfolio/images/')
    url = models.URLField(blank=True)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
