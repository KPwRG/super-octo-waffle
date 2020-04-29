from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("register", views.registerUser),
    path("home", views.home),
    path("logout", views.logout),
    path("login", views.login),
    path("quote/add", views.quoteAdd),
    path("createQuote", views.create),
    path("addtoFav/<int:quoteId>", views.addToFav),
    path("removefromFav/<int:quoteId>", views.removefromFav),
    path("delete/<int:quoteId>", views.deleteQuote),
    path("edit/<int:quoteId>", views.editQuote),
    path("createEdit/<int:quoteId>", views.createEdit),
    path("quote/<int:uploaderId>", views.showQuote),
    
]