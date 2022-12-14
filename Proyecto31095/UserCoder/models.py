from distutils.command import upload
from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

class Message(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    message = models.TextField(max_length=300)