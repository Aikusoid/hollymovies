# Generated by Django 3.2.9 on 2021-11-19 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, default='')),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
