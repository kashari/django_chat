from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(blank=False, null=False, unique=True, max_length=32)
    email = models.EmailField(unique=True)
    password = models.CharField(blank=False, null=False, max_length=45)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username}"
