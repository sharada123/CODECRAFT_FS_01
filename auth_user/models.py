from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta
import datetime
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role_choices = (('admin', 'admin'),('user', 'user'),)
    role = models.CharField(max_length=5, choices=role_choices)
    confirm_password = models.CharField(max_length=10)
    def __str__(self):
        return self.username
class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=now)
    is_used = models.BooleanField(default=False)
    def is_valid(self):
        expiration_time = self.created_at + timedelta(minutes=5)  # OTP is valid for 5 minutes
        return now() <= expiration_time and not self.is_used
