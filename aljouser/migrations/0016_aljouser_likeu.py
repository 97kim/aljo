# Generated by Django 3.1 on 2020-12-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aljouser', '0015_remove_aljouser_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='aljouser',
            name='likeU',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='LIKE'),
        ),
    ]
