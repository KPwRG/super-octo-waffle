from django.shortcuts import render, redirect
from .models import User, Quote
from django.contrib import messages
import bcrypt
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


def registerUser(request):
    errors = User.objects.regisValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    hashedPW = bcrypt.hashpw(
        request.POST['pw'].encode(), bcrypt.gensalt()).decode()
    newuser = User.objects.create(
        firstName=request.POST['fname'], lastName=request.POST['lname'], email=request.POST['email'], password=hashedPW)
    request.session['loggedinId'] = newuser.id
    return redirect("/home")


def home(request):
    if 'loggedinId' not in request.session:
        return redirect("/")
    loggedinuser = User.objects.get(id=request.session['loggedinId'])
    context = {
        'loggedinUser': loggedinuser,
        'myQuotes': Quote.objects.filter(Q(uploader=loggedinuser) | Q(favoritor=loggedinuser)),
        'notMyQuotes': Quote.objects.exclude(Q(uploader=loggedinuser) | Q(favoritor=loggedinuser))
    }

    return render(request, "home.html", context)


def logout(request):
    request.session.clear()
    return redirect("/")


def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    user = User.objects.get(email=request.POST['email'])
    request.session['loggedinId'] = user.id
    return redirect("/home")


def quoteAdd(request):
    return render(request, "addQuote.html")


def create(request):
    errors = Quote.objects.validateQuote(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/quote/add')
    loggedinuser = User.objects.get(id=request.session['loggedinId'])

    newQuote = Quote.objects.create(
        quoterName=request.POST['quoterName'], quote=request.POST['quote'], uploader=loggedinuser)
    return redirect("/home")


def addToFav(request, quoteId):
    loggedinuser = User.objects.get(id=request.session['loggedinId'])
    quote = Quote.objects.get(id=quoteId)
    quote.favoritor.add(loggedinuser)
    return redirect("/home")


def removefromFav(request, quoteId):
    loggedinuser = User.objects.get(id=request.session['loggedinId'])
    quote = Quote.objects.get(id=quoteId)
    quote.favoritor.remove(loggedinuser)
    return redirect("/home")


def deleteQuote(request, quoteId):
    quote = Quote.objects.get(id=quoteId)
    quote.delete()
    return redirect("/home")


def showQuote(request, uploaderId):
    userToShow = Quote.objects.get(id=uploaderId)
    context = {
        'userInfo': userToShow,
        'userQuotes': Quote.objects.filter(uploader=uploaderId)
    }
    return render(request, "showQuote.html", context)

def editQuote(request, quoteId):
    quoteToEdit = Quote.objects.get(id=quoteId)
    context = {
        "quote": quoteToEdit
    }
    return render(request, "edit.html", context)

def createEdit(request, quoteId):
    errors = Quote.objects.validateQuote(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/'+str(quoteId))
    loggedinuser = User.objects.get(id=request.session['loggedinId'])
    editQuote = Quote.objects.get(id=quoteId)
    editQuote.quoterName=request.POST['quoterName']
    editQuote.quote=request.POST['quote'] 
    editQuote.uploader=loggedinuser
    editQuote.save()
    messages.success(request, "Quote successfull updated")
    return redirect("/home")