from tkinter import Image
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profilepics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        MAX_SIZE = 256

        if img.height > MAX_SIZE or img.width > MAX_SIZE:
            img.thumbnail((MAX_SIZE, MAX_SIZE))
            img.save(self.image.path)