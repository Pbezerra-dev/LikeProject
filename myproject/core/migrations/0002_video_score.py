# Generated by Django 2.2.4 on 2019-08-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
