from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Trip
import bcrypt



def index(request):
    return render(request, "index.html")


def register(request):
    errors = User.objects.regis_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(name=request.POST['name'], userName=request.POST['userName'], password=pw_hash)
    request.session['loggedIn'] = newUser.id
    return redirect('/home')

def home(request):
    if 'loggedIn' not in request.session:
        return redirect('/')
    loggedUser = User.objects.get(id=request.session['loggedIn'])
    context = {
        'loggedUser': loggedUser,
        'userTrips': Trip.objects.filter(travler=loggedUser),
        'allTrips': Trip.objects.exclude(travler=loggedUser),
    }
    return render(request, "home.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user = User.objects.get(userName=request.POST['userName'])
    request.session['loggedIn'] = user.id
    return redirect('/home')

def addTrip(request):
    return render(request, "addTrip.html")

def create(request):
    errors = Trip.objects.validateItem(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value) 
        return redirect('/add')
    loggedUser = User.objects.get(id=request.session['loggedIn'])
    newTrip = Trip.objects.create(dest=request.POST['dest'], desc=request.POST['desc'], tdFrom=request.POST['tdFrom'], tdTo=request.POST['tdTo'], travler=loggedUser)
    return redirect('/home')

def destin(request, tripId):
    context = {
        'tripToShow': Trip.objects.get(id=tripId)
    }
    return render(request, "trip.html", context)

def joinTrip(request, tripId):
    loggedUser = User.objects.get(id = request.session['loggedIn'])
    tripAdded = Trip.objects.get(id=tripId)
    tripAdded.travler.add(loggedUser)
    return redirect("/home")
