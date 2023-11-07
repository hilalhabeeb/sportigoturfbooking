from django import forms
from .models import TurfListing

class TurfListingForm(forms.ModelForm):
    class Meta:
        model = TurfListing
        fields = ['turf_name', 'sports_type', 'description', 'price_per_hour', 'location',  'available_from', 'available_to', 'image']
