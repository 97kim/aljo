# Generated by Django 3.1 on 2020-11-30 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aljoadmin', '0011_auto_20201130_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='aljo',
        ),
    ]