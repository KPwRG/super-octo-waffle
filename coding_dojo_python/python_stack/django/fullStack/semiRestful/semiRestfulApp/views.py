from django.shortcuts import render, HttpResponse, redirect
from .models import Shows

def index(request):
    return redirect('/shows')

def shows(request):
    allShows = Shows.objects.all()
    context = {
        'shows': allShows
    }
    return render(request, "shows.html", context)

def addShow(request):
    return render(request, "addShow.html")

def showId(request, showId):
    showId = Shows.objects.get(id=showId)
    context = {
        'show': showId
    }
    return render(request, "showId.html", context)

def showEdit(request, showId):
    showToUpdate = Shows.objects.get(id=showId)
    context = {
        'show': showToUpdate
    }
    return render(request, "showEdit.html", context)

def showUpdate(request):

    return redirect(f'/shows/'+str(showId))

def showDelete(request, showId):
    return redirect('/shows')