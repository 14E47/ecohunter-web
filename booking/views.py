from django.shortcuts import render

from datetime import datetime, timedelta
from django.utils import timezone
# Create your views here.

def room_availability(request):
    # created_time_limit = timezone.now() - timedelta(hours=12)
    # latest_news_post = Post.objects.filter(created__gte=created_time_limit)
    data = []
    return JsonResponse({'data': data})