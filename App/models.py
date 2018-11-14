from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Est(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        """A string shit"""
        return self.title

class PersonaTest(AbstractUser):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    usname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.email