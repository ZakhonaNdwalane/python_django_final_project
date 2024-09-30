from django.contrib import admin

from .models import Farm, Crop, DataEntry

# Register your models here.
admin.site.register(Farm)
admin.site.register(Crop)
admin.site.register(DataEntry)
