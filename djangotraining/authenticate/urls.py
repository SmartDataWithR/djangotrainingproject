from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    # authentication
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password', change_password, name='change_password'),

]