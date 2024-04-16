from django.contrib import admin
from .models import *

 
# Register your models here.
admin.site.register(Usertable)
admin.site.register(TurfProvider)
admin.site.register(TurfListing)
admin.site.register(Booking)
admin.site.register(ClubUser)