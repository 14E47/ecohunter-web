from django.conf.urls import url, include
from experience import views

urlpatterns = [
    url("^$", views.experience_list, name='experience_list'),
    url("^(?P<slug>.*)/$",views.experience_detail, name="experience-detail"),
]