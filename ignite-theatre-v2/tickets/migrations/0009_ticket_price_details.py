# Generated by Django 3.2.7 on 2022-10-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20221027_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='price_details',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
