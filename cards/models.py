from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class JobCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)