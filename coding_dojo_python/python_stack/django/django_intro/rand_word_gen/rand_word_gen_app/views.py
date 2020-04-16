from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1

    if request.session['counter'] <= 1:
        random_word = ""
    else:
        random_word = get_random_string(length=14)
    context = {
        'randomWord' : random_word
    }
    return render(request, "randomWord.html", context)

def generate(request):
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")