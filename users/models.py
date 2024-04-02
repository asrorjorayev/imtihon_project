from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image=models.ImageField(upload_to='user_image',null=True,blank=True,default="")
    phone_number=models.CharField(max_length=13,null=True,blank=True)
