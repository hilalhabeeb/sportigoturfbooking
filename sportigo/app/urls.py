from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name="index"),
    path('signup/', signup, name="signup"),
    path('user_login/', user_login, name="user_login"),
    path('index2/', index2, name="index2"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('check_user_exists/', check_user_exists, name='check_user_exists'),
    path('logout/', userLogout, name="logout"),
    path('forgotPassword/', forgotPassword, name="forgotPassword"),
    path('adminreg/', adminreg, name="adminreg"),
    path('userprofile/', user_profile, name="user_profile"),
    path('update_user_details/', update_user_details, name="update_user_details"),  # Add this line
    path('turfproviderreg/', turfproviderreg, name="turfproviderreg"),
    path('provider_update/', provider_update, name='provider_update'),
    path('providerhome/', providerhome, name='providerhome'),
    path('add_turf/',add_turf, name='add_turf'),
    path('turf_detail/<int:turf_id>/', turf_detail, name='turf_detail'),
    path('manage_turf/<int:turf_id>/', manage_turf, name='manage_turf'),
    path('change_password/',change_password, name='change_password'),
    path('booking_history/',booking_history, name='booking_history'),
    
    path('search/',search, name='search'),






]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)