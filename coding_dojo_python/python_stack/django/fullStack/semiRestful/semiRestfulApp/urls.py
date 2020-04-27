from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new',views.addShow),
    path('shows/<int:showId>', views.showId),
    path('shows/<int:showId>/edit', views.showEdit),
    path('shows/update', views.showUpdate),
    path('shows/delete', views.showDelete),
]