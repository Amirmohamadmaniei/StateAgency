# Generated by Django 4.1 on 2022-08-22 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_requestvisit_property_alter_requestvisit_agent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='user',
        ),
    ]