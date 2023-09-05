from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
