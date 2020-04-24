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

def showBook(request, bookId):
    bookToShow = Books.objects.get(id=bookId)
    context = {
        'bookInfo': bookToShow,
        'bookAuthors': Authors.objects.filter(books=bookId),
        'allAuthors': Authors.objects.all()
    }
    return render(request, 'bookId.html', context)

def addAuthorToBook(request, bookId):
    book = Books.objects.get(id=bookId)
    authorAdded = Authors.objects.get(id= request.POST['authorId'])
    authorAdded.books.add(book)
    return redirect('/books/<bookId>')