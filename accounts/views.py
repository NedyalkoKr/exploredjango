from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
)

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
