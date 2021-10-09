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
    image = models.ImageField(default= "default.png")

    def __str__(self):
        return self.user.username + " Profile"

    # def save(self):
    #     super().save()
    #
    #     imag = Image.open(self.image.path)
    #     if imag.height >400 or imag.width >400:
    #         output_size = imag(400,400)
    #         imag.thumbnail(output_size)
    #         imag.save(self.image.path)




