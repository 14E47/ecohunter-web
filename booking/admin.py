from django.contrib import admin

from .models import Booking
from experience.models import Experience ,ExperienceImage
# Register your models here.

admin.site.register(Booking)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'slug', 'duration', 'seats', 'slot')

admin.site.register(Experience, ExperienceAdmin)   


class ExperienceImageAdmin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(ExperienceImage, ExperienceImageAdmin)