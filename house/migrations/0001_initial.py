# Generated by Django 4.1 on 2022-08-19 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('cost', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('status', models.CharField(choices=[('sale', 'sale'), ('rent', 'rent')], max_length=10)),
                ('type', models.CharField(choices=[('shop', 'shop'), ('house', 'house')], max_length=10)),
                ('area', models.IntegerField()),
                ('year_created', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('parking', models.BooleanField(default=False)),
                ('warehouse', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/house')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='house.property')),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='house.property')),
            ],
        ),
    ]
