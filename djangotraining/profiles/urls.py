from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [
    # authentication
    path('edit_basic_profile/', edit_basic_profile, name='edit_basic_profile'),
]