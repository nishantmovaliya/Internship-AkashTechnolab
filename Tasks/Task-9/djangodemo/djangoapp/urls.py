from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.indexpageview,name='index'),
    path('/signup',views.signuppageview,name='signup'),
    path('/about',views.aboutpageview,name='about'),
    path('/contact',views.contactpageview,name='contact'),
    path('/display',views.displaypageview,name='display'),
]


