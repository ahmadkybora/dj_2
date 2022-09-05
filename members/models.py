from pyexpat import model
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200, verbose_name="نام کاربری")
