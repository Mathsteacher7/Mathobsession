from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # custom fields here...
    image = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
