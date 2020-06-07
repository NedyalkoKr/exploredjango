from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('pages.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('user/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
