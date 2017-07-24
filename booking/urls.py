from django.conf.urls import url, include
from booking import views

urlpatterns = [
    url(r'^availability/$', views.room_availability, name='availability'),
]
