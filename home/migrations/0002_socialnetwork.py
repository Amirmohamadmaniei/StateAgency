# Generated by Django 4.1 on 2022-08-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('telegram', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
    ]
