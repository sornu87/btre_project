# Generated by Django 2.0.5 on 2018-10-24 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='photo_2',
        ),
    ]
