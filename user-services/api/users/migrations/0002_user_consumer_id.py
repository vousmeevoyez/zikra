# Generated by Django 3.0.5 on 2020-04-18 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='consumer_id',
            field=models.UUIDField(null=True),
        ),
    ]
