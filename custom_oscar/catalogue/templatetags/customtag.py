from django import template

from booking.models import Booking
from django.conf import settings
from experience.models import Experience

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
    data = response.json()

    feeds = []
    for index in data:
        feed = {}
        image = index['featured_media']
        i_image = requests.get(BLOG_URL + "/blog/wp-json/wp/v2/media/"+str(image))
        i_response_data = i_image.text
        i_data = json.loads(i_response_data)
        feed['title'] = index['title']['rendered']
        feed['description'] = index['excerpt']['rendered']
        feed['image'] = i_data['guid']
        feed['link'] = index['link']
        feeds.append(feed) 
    return feeds


@register.assignment_tag
def top_experiences():
    top_experiences = Experience.objects.all()
    return top_experiences
