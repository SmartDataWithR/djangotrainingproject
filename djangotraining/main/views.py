from django.shortcuts import render, redirect
from django.contrib import messages
from authenticate.views import *


def index(request):
    return render(request, 'index.html', {})