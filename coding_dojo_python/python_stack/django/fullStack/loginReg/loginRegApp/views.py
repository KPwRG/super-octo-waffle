from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Registration

def index(request):
    return HttpResponse("KPwRG")
