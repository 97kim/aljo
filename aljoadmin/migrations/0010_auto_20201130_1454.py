# Generated by Django 3.1 on 2020-11-30 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aljoadmin', '0009_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='aljo',
            new_name='aljoadmin',
        ),
    ]
