# Generated by Django 5.2.4 on 2025-07-26 11:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("published_date", models.DateField()),
                ("author", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=100)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("published_date", models.DateField(default=django.utils.timezone.now)),
                ("isbn_number", models.CharField(max_length=13, unique=True)),
                ("pages", models.IntegerField(default=0)),
                ("cover_image", models.ImageField(upload_to="covers/")),
                ("language", models.CharField(max_length=30)),
            ],
        ),
    ]
