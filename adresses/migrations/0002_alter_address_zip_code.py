# Generated by Django 4.2.5 on 2023-09-05 15:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adresses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="zip_code",
            field=models.IntegerField(),
        ),
    ]
