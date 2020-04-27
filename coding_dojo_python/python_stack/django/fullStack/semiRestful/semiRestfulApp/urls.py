from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/addShow',views.addShow),
    path('shows/createNewShow',views.createNewShow),
    path('shows/<int:showId>', views.showId),
    path('shows/<int:showId>/edit', views.showEdit),
    path('shows/<int:showId>/update', views.showUpdate),
    path('shows/<int:showId>/delete', views.showDelete),
]