from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'lbs_app/index.html')


def register(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)

        if regform.is_valid():
            regform.save()
            return redirect('login')
    else:
        regform = UserCreationForm()
    return render(request, 'lbs_app/register.html', {'form': regform})


def maps(request):
    return render(request, 'lbs_app/map.html')
