from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('createBook', views.createBook),
    path('books/<bookId>', views.showBook),
    path('addAuthorToBook/<bookId>', views.addAuthorToBook),	   
]