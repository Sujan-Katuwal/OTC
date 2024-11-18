from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class MyCustomUser(AbstractBaseUser):
        ROLE_CHOICE = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
        role = models.CharField(max_length=10, choices=ROLE_CHOICE, default='user')
        email = models.EmailField(max_length=255, unique=True)
        

        
