# Generated by Django 2.1.7 on 2019-03-13 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
