# Generated by Django 3.2.7 on 2022-10-25 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0004_cast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='role',
        ),
    ]
