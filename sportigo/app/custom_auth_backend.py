
from django.contrib.auth.backends import BaseBackend
from .models import ClubUser

class ClubUserAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = ClubUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except ClubUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return ClubUser.objects.get(pk=user_id)
        except ClubUser.DoesNotExist:
            return None
