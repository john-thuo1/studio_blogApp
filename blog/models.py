from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.title
    
    # Returns path to any specific post instance.
    # In our case, once you create a post, you will be directed to the post detail page
    # use reverse method to return the complete URL to the route as a string
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        
