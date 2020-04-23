from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Authors

def index(request):
    allBooks = Books.objects.all()
    context = {
        'books': allBooks
    }
    return render(request,"book.html", context)

def createBook(request):
    newBook = Books.objects.create(title = request.POST['bookTitle'], desc = request.POST['description'])
    return redirect('/')