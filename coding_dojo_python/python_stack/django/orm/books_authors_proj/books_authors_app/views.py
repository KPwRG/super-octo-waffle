from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Authors

def index(request):
    allBooks = Books.objects.all()
    context = {
        'books': allBooks
    }
    return render(request,"book.html", context)

def authors(request):
    allAuthors = Authors.objects.all()
    context = {
        'authors': allAuthors
    }
    return render(request, "author.html", context)

def createBook(request):
    newBook = Books.objects.create(title = request.POST['bookTitle'], desc = request.POST['description'])
    return redirect('/')

def createAuthor(request):
    newAuthor = Authors.objects.create(first_name=request.POST['firstName'], last_name=request.POST['lastName'], notes=request.POST['notes'])
    return redirect('/authors')

def showBook(request, bookId):
    bookToShow = Books.objects.get(id=bookId)
    context = {
        'bookInfo': bookToShow,
        'bookAuthors': Authors.objects.filter(books=bookId),
        'allAuthors': Authors.objects.exclude(books=bookId)
    }
    return render(request, 'bookId.html', context)

def showAuthor(request, authorId):
    authorToShow = Authors.objects.get(id=authorId)
    context = {
        'authorInfo': authorToShow,
        'authorBooks': Books.objects.filter(authors=authorId),
        'allBooks': Books.objects.exclude(authors=authorId)
    }
    return render(request, 'authorId.html', context)

def addAuthorToBook(request, bookId):
    book = Books.objects.get(id=bookId)
    authorAdded = Authors.objects.get(id= request.POST['authorId'])
    authorAdded.books.add(book)
    return redirect(f'/books/'+str(bookId))

def addBookToAuthor(request, authorId):
    author = Authors.objects.get(id=authorId)
    bookAdded = Books.objects.get(id=request.POST['bookId'])
    bookAdded.authors.add(author)
    return redirect(f'/authors/'+str(authorId))