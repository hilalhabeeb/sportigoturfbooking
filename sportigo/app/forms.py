from django import forms
from .models import TurfListing, TurfImage

class TurfListingForm(forms.ModelForm):
    class Meta:
        model = TurfListing
        fields = ['turf_name', 'sports_type', 'description', 'price_per_hour','price_per_day', 'location', 'available_from', 'available_to']

from multiupload.fields import MultiFileField

class TurfImageForm(forms.ModelForm):
    images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)  # Adjust min_num, max_num, and max_file_size as needed

    class Meta:
        model = TurfImage
        fields = ['images']


from django import forms
from .models import FAQ

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']

        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your question'}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your answer', 'rows': 4}),
        }
