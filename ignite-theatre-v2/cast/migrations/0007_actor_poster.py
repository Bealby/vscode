# Generated by Django 3.2.7 on 2022-10-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0006_actor_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
