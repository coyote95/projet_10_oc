# Generated by Django 3.2.5 on 2024-02-22 22:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(150),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="can_be_contacted",
            field=models.BooleanField(default=False, verbose_name="Peut-être contacté?"),
        ),
        migrations.AlterField(
            model_name="user",
            name="can_data_be_shared",
            field=models.BooleanField(default=False, verbose_name="Partager les données?"),
        ),
    ]
