from __future__ import unicode_literals
from django.contrib.sites.models import Site
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.core.urlresolvers import reverse

class Experience(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    product_title = models.CharField(max_length=50, unique=True)
    duration = models.CharField(max_length=50,default=None)
    seats = models.CharField(max_length=50, default=None)
    slot = models.CharField(max_length=50, default=None)
    activity = models.CharField(max_length=50, default=None)
    the_experience = models.TextField(blank=True, null=True)
    the_activity = models.TextField(blank=True, null=True)
    Accomodation = models.TextField(blank=True, null=True)
    practical = models.TextField(blank=True, null=True)
#    product_image = models.ImageField(default=None)

    class Meta:
        verbose_name = "experience"
        verbose_name_plural = "experience"

    def __str__(self):
        return '%s' % self.product_title

    def get_absolute_url(self):
        return "/experience/%s" % self.slug


    def images(self):
        images = ExperienceImage.objects.filter(experience=self)
        return images

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.product_title)
        super(Experience, self).save(*args, **kwargs)

class ExperienceImage(models.Model):
    image = models.ImageField(blank=True, upload_to='uploads/images')
    experience = models.ForeignKey(Experience)

    class Meta:
        verbose_name = "experience Image"
        verbose_name_plural = "experience Images"        
