from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from PIL import Image

# Create your models here.





class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = CloudinaryField('image')

    def __str__(self):
        return self.user.username + " Profile"






