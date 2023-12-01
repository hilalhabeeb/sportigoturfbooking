from django import forms
from .models import TurfListing, TurfImage

class TurfListingForm(forms.ModelForm):
    class Meta:
        model = TurfListing
        fields = ['turf_name', 'sports_type', 'description', 'price_per_hour', 'location', 'available_from', 'available_to']

from multiupload.fields import MultiFileField

class TurfImageForm(forms.ModelForm):
    images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)  # Adjust min_num, max_num, and max_file_size as needed

    class Meta:
        model = TurfImage
        fields = ['images']