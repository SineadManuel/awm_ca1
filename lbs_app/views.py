from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from django.http import JsonResponse
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


@login_required
def update_database(request):
    my_location = request.POST.get("point", None)
    if not my_location:
        return JsonResponse({"message": "No location found."}, status=400)

    try:
        my_coords = [float(coord) for coord in my_location.split(", ")]
        my_profile = request.user
        my_profile.last_location = Point(my_coords)
        my_profile.save()

        message = f"Updated {request.user.username} with {f'POINT({my_location})'}"

        return JsonResponse({"message": message}, status=200)
    except:
        return JsonResponse({"message": "No profile found."}, status=400)
