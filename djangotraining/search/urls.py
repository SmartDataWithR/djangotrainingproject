from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    url(r'^ajax_calls/search/', views.autocompleteModel),
]