from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta
from django.utils import timezone
from booking.forms import BookingQueryForm
from django.http import HttpResponseRedirect
# Create your views here.

def room_availability(request):
    # created_time_limit = timezone.now() - timedelta(hours=12)
    # latest_news_post = Post.objects.filter(created__gte=created_time_limit)
    data = []
    return JsonResponse({'data': data})

@login_required
def booking_query(request):
    form = BookingQueryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # messages.success(request, 'Thank you for your query posted. We shall reply shortly at your registered email address.')
            # reciepient_name = request.user.first_name
            # reciepient_email = request.user.email
            # subject = "Ecohunter | Response to your 'My Question' query" 
            # mail = "Hi %s,\n\nThank you for your query posted under the 'My Question' section.\n\nWe shall reply to your query shortly.\n\nThanks,\nTeam Famhealth" % (reciepient_name)
            # email = EmailMessage(subject, mail, to=[reciepient_email])
            # email.send()

	return HttpResponseRedirect('/')