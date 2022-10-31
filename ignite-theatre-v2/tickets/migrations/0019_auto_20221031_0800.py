# Generated by Django 3.2.7 on 2022-10-31 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0018_auto_20221030_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='price',
            new_name='price_adult',
        ),
        migrations.AddField(
            model_name='ticket',
            name='price_child',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
