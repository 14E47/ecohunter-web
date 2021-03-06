from django.contrib import admin
from .models import Booking, BookingQuery
#from experience.models import Experience ,ExperienceImage
# Register your models here.

from experience.models import Experience, ExperienceImage

class ExperienceImageInline(admin.TabularInline):
    model = ExperienceImage

class ExperienceImageAdmin(admin.ModelAdmin):
    inlines = [ExperienceImageInline]

admin.site.register(Booking)
admin.site.register(BookingQuery)
admin.site.register(Experience ,ExperienceImageAdmin)
