from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.maps, name='map'),
    path('register/', views.register, name='register'),
]
