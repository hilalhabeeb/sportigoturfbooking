from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from app import candy


urlpatterns = [
    *candy.path('', index, name="index"),
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
    path('update_user_details/', update_user_details, name="update_user_details"), 
    path('turfproviderreg/', turfproviderreg, name="turfproviderreg"),
    path('provider_update/', provider_update, name='provider_update'),
    path('club_update/', club_update, name='club_update'),
    path('providerhome/', providerhome, name='providerhome'),
    path('add_turf/',add_turf, name='add_turf'),
    path('register_club_user/', register_club_user, name='register_club_user'),
    path('clubhome/',clubhome, name='clubhome'),
    
    
    
    path('manage_turf/<int:turf_id>/', manage_turf, name='manage_turf'),
    path('change_password/',change_password, name='change_password'),
    path('turf_detail/<int:turf_id>/', turf_detail, name='turf_detail'),
    path('turf_detail2/<int:turf_id>/', turf_detail2, name='turf_detail2'),
    path('booking_history/',booking_history, name='booking_history'),
    path('club_booking_history/',club_booking_history, name='club_booking_history'),
    path('confirmation/',confirmation, name='confirmation'),
    path('confirmation2/',confirmation2, name='confirmation2'),
    path('search/',search, name='search'),
    path('faq/',faq, name='faq'),
    path('cancel_booking/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('weather_prediction/', weather_prediction, name='weather_prediction'),
    path('download_receipt/<int:booking_id>/', download_receipt, name='download_receipt'),
    path('find_nearest_turf_view/', find_nearest_turf_view, name='find_nearest_turf_view'),
    path('manage-faqs/', manage_faqs, name='manage_faqs'),
    path('delete-faq/<int:faq_id>/', delete_faq, name='delete_faq'),
 
   



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)