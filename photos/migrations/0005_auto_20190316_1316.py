# Generated by Django 2.1.7 on 2019-03-16 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_auto_20190316_1316'),
        ('photos', '0004_remove_photo_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='category',
        ),
        migrations.AddField(
            model_name='photo',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.Subcategory'),
        ),
    ]
