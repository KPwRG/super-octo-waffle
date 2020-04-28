from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
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
    newUser = User.objects.create(firstName=request.POST['firstName'], lastName=request.POST['lastName'], email=request.POST['email'], password=pw_hash)
    request.session['loggedIn'] = newUser.id
    return redirect('/home')

def home(request):
    if 'loggedIn' not in request.session:
        return redirect('/')
    context = {
        'loggedUser': User.objects.get(id=request.session['loggedIn'])
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
    user = User.objects.get(email=request.POST['email'])
    request.session['loggedIn'] = user.id
    return redirect('/home')
