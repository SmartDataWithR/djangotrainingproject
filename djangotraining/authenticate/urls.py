from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [
    # authentication
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('change_password', change_password, name='change_password'),
    path('', include('django.contrib.auth.urls')),
]