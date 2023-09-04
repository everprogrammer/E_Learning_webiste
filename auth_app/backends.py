from typing import Any, Optional
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Q
from django.http.request import HttpRequest

UserModel = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username_or_email=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
        except UserModel.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        
        return None