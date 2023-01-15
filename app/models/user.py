from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=32)
    recent_accounts = models.JSONField(null=True, blank=True)
    favorite_accounts = models.JSONField(null=True, blank=True)
