from django import template

from booking.models import Booking
import pdb

register = template.Library()

from oscar.apps.catalogue.models import Product

@register.assignment_tag
def top_products():
	top_products = Product.objects.filter(parent__isnull=True).order_by('-date_updated')[:6]
	return top_products