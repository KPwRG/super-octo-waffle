from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
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

def createNewShow(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/addShow')
    else:
        newShow = Shows.objects.create(title=request.POST['showTitle'], network=request.POST['showNetwork'], release_date=request.POST['showReleaseDate'], desc=request.POST['description'])
    showId = newShow.id
    return redirect(f'/shows/'+str(showId))

def showId(request, showId):
    showId = Shows.objects.get(id=showId)
    context = {
        'show': showId
    }
    return render(request, "showId.html", context)

def showEdit(request, showId):
    showToEdit = Shows.objects.get(id=showId)
    context = {
        'show': showToEdit
    }
    return render(request, "showEdit.html", context)

def showUpdate(request, showId):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/'+str(showId)+'/edit')
    else:
        showToUpdate = Shows.objects.get(id=showId)
        showToUpdate.title = request.POST['showTitle']
        showToUpdate.network = request.POST['showNetwork']
        showToUpdate.realease_date = request.POST['showReleaseDate']
        showToUpdate.desc = request.POST['description']
        showToUpdate.save()
        messages.success(request, "Show successfully updated")
    return redirect(f'/shows/'+str(showId))

def showDelete(request, showId):
    showToDelete = Shows.objects.get(id=showId)
    showToDelete.delete()
    return redirect('/shows')