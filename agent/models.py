from django.db import models
from django.urls import reverse


class Agent(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='img/agent')
    bio = models.TextField()
    phone = models.CharField(max_length=11, unique=True)
    instagram = models.CharField(max_length=80, unique=True)
    telegram = models.CharField(max_length=80, unique=True)
    whatsapp = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('agent:detail_agent', kwargs={'pk': self.pk})
