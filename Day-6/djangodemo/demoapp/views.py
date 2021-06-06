from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepageview(request):
    return HttpResponse("<h1>Hello Nishant, Welcome to the Django...!</h1>")
