# Generated by Django 5.0.6 on 2024-05-19 04:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_video_link_alter_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video_link',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(verbose_name=datetime.date.today),
        ),
    ]
