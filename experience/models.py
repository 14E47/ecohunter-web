from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

class Experience(models.Model):
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "experience"
        verbose_name_plural = "experience"

    def __unicode__(self):
        return '%s' % self.slug

    def get_absolute_url(self):
        return self.slug

    def images(self):
        images = ExperienceImage.objects.filter(experience=self)
        return images

    def name(self):
        name = ExperienceName.objects.filter(experience=self)
        return name


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.images)
            self.slug = slugify(self.name)
        super(Experience, self).save(*args, **kwargs)

class ExperienceImage(models.Model):
    image = models.ImageField(blank=True, upload_to='uploads/images')
    experience = models.ForeignKey(Experience)

    class Meta:
        verbose_name = "experience Image"
        verbose_name_plural = "experience Images"        