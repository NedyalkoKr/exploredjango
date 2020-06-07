from django.urls import path
from django.contrib.auth.views import (
    LoginView,
)
from .views import UserLoginView

urlpatterns = [
    # custoimize View behaviour
    # path('user/login/', LoginView.as_view(), name='user_login'),
    #path('login/', UserLoginView.as_view(), name='user_login'),
]