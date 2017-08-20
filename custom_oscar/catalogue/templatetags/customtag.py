from django import template

from booking.models import Booking
from django.conf import settings

import pdb
import requests, json

register = template.Library()

from oscar.apps.catalogue.models import Product

@register.assignment_tag
def top_products():
	top_products = Product.objects.filter(parent__isnull=True).order_by('-date_updated')[:6]
	return top_products


@register.assignment_tag
def wordpress_feeds():
	BLOG_LENGTH = getattr(settings, 'BLOG_MAX_LENGTH', None)
	BLOG_URL = getattr(settings, 'BLOG_URL', None)

	response = requests.get(BLOG_URL + "/blog/wp-json/wp/v2/posts")
	response_data = response.content
	data = json.loads(response_data)

	feeds = []
	for index in data:
	    feed = {}
	    image = index['featured_media']
	    i_image = requests.get(BLOG_URL + "/blog/wp-json/wp/v2/media/"+str(image))
	    i_response_data = i_image.text
	    i_data = json.loads(i_response_data)
	    feed['slug'] = index['slug']
	    feed['description'] = index['excerpt']['rendered']
	    feed['image'] = i_data['guid']
	    feeds.append(feed)

	return feeds