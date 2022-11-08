from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'lbs_app/index.html')


def register(request):
    return render(request, 'lbs_app/register.html')


def login(request):
    return render(request, 'lbs_app/login.html')


def maps(request):
    return render(request, 'lbs_app/map.html')


def logout(request):
    return render(request, 'lbs_app/logout.html')


