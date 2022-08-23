from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    sub = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.sub


class SocialNetwork(models.Model):
    whatsapp = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()

