# Generated by Django 3.1 on 2020-12-01 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aljoadmin', '0020_aljoadmin_likes_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aljoadmin',
            name='likes_user',
        ),
    ]
