from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role_choices = (('admin', 'admin'),('user', 'user'),)
    role = models.CharField(max_length=5, choices=role_choices)
    confirm_password = models.CharField(max_length=10)
    def __str__(self):
        return self.username
