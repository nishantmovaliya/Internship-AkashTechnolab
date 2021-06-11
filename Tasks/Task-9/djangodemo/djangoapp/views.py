from os import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexpageview(request):
    return render('index.html')

def signuppageview(request):
    return render('signup.html')

def aboutpageview(request):
    return render('about.html')

def contactpageview(request):
    return render('contact.html')

