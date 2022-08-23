from django.contrib import admin
from . import models


class ImageAdmin(admin.StackedInline):
    model = models.Image


class AmenityAdmin(admin.StackedInline):
    model = models.Amenity


class HouseAdmin(admin.ModelAdmin):
    inlines = [AmenityAdmin, ImageAdmin]

    class Meta:
        model = models.Property


admin.site.register(models.Image)
admin.site.register(models.Property, HouseAdmin)

admin.site.register(models.RequestVisit)
