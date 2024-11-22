from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    username = models.CharField(max_length=120, unique=True)
