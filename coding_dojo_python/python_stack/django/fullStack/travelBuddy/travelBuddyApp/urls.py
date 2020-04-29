from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('home', views.home),
    path('logout', views.logout),
    path('login', views.login),
    path('create', views.create),
    path('add', views.addTrip),
    path('join/<int:tripId>', views.joinTrip),
    path('destination/<int:tripId>', views.destin),	   
]