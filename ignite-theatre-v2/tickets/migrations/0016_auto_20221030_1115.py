# Generated by Django 3.2.7 on 2022-10-30 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0015_auto_20221030_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='price_adult',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='price_child',
        ),
    ]
