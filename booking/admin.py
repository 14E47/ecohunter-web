from django.contrib import admin

from .models import Booking
from experience.models import Experience ,ExperienceImage
# Register your models here.

admin.site.register(Booking)
admin.site.register(Experience)
admin.site.register(ExperienceImage)
