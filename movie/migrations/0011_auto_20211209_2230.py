# Generated by Django 3.2.9 on 2021-12-09 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_auto_20211209_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='finances',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cinemamovieshowings',
            name='ticket_price',
            field=models.FloatField(),
        ),
    ]
