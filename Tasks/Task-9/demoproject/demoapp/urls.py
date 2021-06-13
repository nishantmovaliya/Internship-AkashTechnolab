from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexpage,name='index'),
    path('signup',views.signuppage,name='signup'),
    path('about',views.aboutpage,name='about'),
    path('contact',views.contactpage,name='contact'),
    path('formprocess',views.process,name='process'),
]
