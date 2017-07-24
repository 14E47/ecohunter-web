from __future__ import unicode_literals

from django.db import models

from oscar.apps.catalogue.models import Product
from oscar.apps.order.models import Order

from django.contrib.auth.models import User
# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User)
    from_date = models.DateTimeField(null=False, blank=False)
    to_date = models.DateTimeField(null=False, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)

    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order)
    rooms = models.CharField(max_length=2)
    guests = models.CharField(max_length=2)

    def __unicode__(self):
        return str(self.date) + " User: " + str(self.user)

    def short_desc(self):
        """Default short description visible on reservation button"""
        return str(self.id)