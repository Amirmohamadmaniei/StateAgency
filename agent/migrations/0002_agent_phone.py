# Generated by Django 4.1 on 2022-08-19 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='phone',
            field=models.CharField(default=1, max_length=11, unique=True),
            preserve_default=False,
        ),
    ]
