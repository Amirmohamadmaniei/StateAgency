from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from account.models import CustomUser
from agent.models import Agent


class Property(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='properties')
    cost = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    address = models.TextField()
    state = (
        ('sale', 'sale'),
        ('rent', 'rent'),
    )
    status = models.CharField(max_length=10, choices=state)
    type = (
        ('shop', 'shop'),
        ('house', 'house'),
    )
    type = models.CharField(max_length=10, choices=type)
    area = models.IntegerField()
    year_created = models.IntegerField()
    floor = models.IntegerField()
    beds = models.IntegerField()
    parking = models.BooleanField(default=False)
    warehouse = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Property, self).save()

    def get_absolute_url(self):
        return reverse('property:detail_property', kwargs={'slug': self.slug})


class Image(models.Model):
    house = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='img/house')


class Amenity(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='amenities')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class RequestVisit(models.Model):
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    message = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


