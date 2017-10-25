from django.conf.urls import url, include
from booking import views

urlpatterns = [
    url(r'^availability/$', views.room_availability, name='availability'),
    url(r'^query/$', views.booking_query, name='booking-query'),
]
