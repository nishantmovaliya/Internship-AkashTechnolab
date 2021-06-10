from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexpage(request):
    return render(request,'index.html')

def formpage(request):
    return render(request,'form.html')

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')