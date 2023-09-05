from django.db import models
import uuid


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    street = models.CharField(max_length=150)
    number = models.CharField(max_length=20, null=True)
    district = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=5)
    zip_code = models.IntegerField()
