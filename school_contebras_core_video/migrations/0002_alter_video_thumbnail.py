# Generated by Django 5.1.1 on 2024-12-08 15:10

import school_contebras_core_video.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_contebras_core_video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(upload_to=school_contebras_core_video.models.random_filename, verbose_name='Thumbnail'),
        ),
    ]
