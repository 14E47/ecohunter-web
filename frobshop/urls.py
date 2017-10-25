"""frobshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

from django.contrib import admin
from experience import urls as experience_urls

from oscar.app import application
from experience import urls as experience_urls
from booking import urls as booking_url
from oscarapi.app import application as api

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^booking/', include(booking_url)),
    url(r'^about/$', TemplateView.as_view(template_name='about-us.html'), name="about-us"),
    url(r'^contact/$', TemplateView.as_view(template_name='contact-us.html'), name="contact-us"),
    url(r'', include(application.urls)),
    url(r'^experience/', include(experience_urls)),
    url(r'^api/', include(api.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Ecohunter'