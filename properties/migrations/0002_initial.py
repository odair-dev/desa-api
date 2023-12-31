# Generated by Django 4.2.5 on 2023-09-05 15:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("schedules", "0001_initial"),
        ("properties", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="schedules",
            field=models.ManyToManyField(
                related_name="my_visits",
                through="schedules.Schedule",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
