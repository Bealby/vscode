# Generated by Django 3.2.7 on 2022-10-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0007_actor_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='poster',
        ),
        migrations.AddField(
            model_name='show',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
