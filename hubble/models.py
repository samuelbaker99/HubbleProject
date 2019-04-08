from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    subtitle = models.CharField(max_length=200, default='')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
class Item(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='auction')
    date_posted = models.DateTimeField(default=timezone.now)
    price = models.CharField(max_length=8)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.pk})
    
    

        
    
    
    