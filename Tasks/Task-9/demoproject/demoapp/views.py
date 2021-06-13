from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexpage(request):
    return render(request,'index.html')

def signuppage(request):
    return render(request,'signup.html')

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')

def process(request):
    print('Welcome')
    print(request.method)
    print(request.POST)
    return render(request,'display.html',{'fname':request.POST['fname'],'lname':request.POST['lname'],
    'gender':request.POST['gender'],'dob':request.POST['birthdate'],
    'country_code':request.POST['country_code'],
    'contact':request.POST['contact'],'email':request.POST['email'],'password':request.POST['password'],
    'retypepass':request.POST['retypepass']})
