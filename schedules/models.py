from django.db import models
import uuid


class HourOptions(models.TextChoices):
    H01 = "8:00"
    H02 = "8:30"
    H03 = "9:00"
    H04 = "9:30"
    H05 = "10:00"
    H06 = "10:30"
    H07 = "11:00"
    H08 = "11:30"
    H09 = "12:00"
    H10 = "12:30"
    H11 = "13:00"
    H12 = "13:30"
    H13 = "14:00"
    H14 = "14:30"
    H15 = "15:00"
    H16 = "15:30"
    H17 = "16:00"
    H18 = "16:30"
    H19 = "17:00"
    H20 = "17:30"
    H21 = "18:00"
    H22 = "18:30"
    H23 = "19:00"
    H24 = "19:30"


class Schedule(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    date = models.DateField()
    hour = models.TimeField(
        choices=HourOptions.choices
    )
    property = models.ForeignKey(
        "properties.Property",
        on_delete=models.CASCADE,
        related_name="my_schedules"
    )
    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="my_schedules"
    )
