# Generated by Django 3.2.9 on 2021-11-20 00:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(default=0,
                                    validators=[django.core.validators.MaxValueValidator(10),
                                                django.core.validators.MinValueValidator(0)]),
        ),
    ]