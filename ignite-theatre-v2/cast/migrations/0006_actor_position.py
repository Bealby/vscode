# Generated by Django 3.2.7 on 2022-10-25 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0005_remove_actor_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='position',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
