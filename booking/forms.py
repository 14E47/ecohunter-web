from django import forms
from booking.models import BookingQuery

class BookingQueryForm(forms.ModelForm):
    class Meta:
        model = BookingQuery
        fields = ('user', 'name', 'email', 'phone', 'travel_dates', 'hotel', 'price', 'type')