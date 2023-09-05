from django.db import models
import uuid


class Property(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    enterprise = models.CharField(max_length=150, unique=True)
    sold = models.BooleanField(default=False)
    address = models.ForeignKey(
        "adresses.Address",
        on_delete=models.PROTECT,
        related_name="properties"
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.PROTECT,
        related_name="properties"
    )
    schedules = models.ManyToManyField(
        "accounts.Account",
        related_name="my_visits",
        through="schedules.Schedule"
    )
