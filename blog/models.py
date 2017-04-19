from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)
  artist1 = models.CharField(max_length=200, null = True)
  artist2 = models.CharField(max_length=200, null = True)
  artist3 = models.CharField(max_length=200, null = True)
  artist4 = models.CharField(max_length=200, null = True)
  artist5 = models.CharField(max_length=200, null = True)  
  
def publish(self):
  self.published_date = timezone.now()
  self.save()
  
def __str__(self):
  return self.title
