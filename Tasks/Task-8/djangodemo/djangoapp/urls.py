from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexpage,name='index'),
    path('form',views.formpage,name='form'),
    path('about',views.aboutpage,name='about'),
    path('contact',views.contactpage,name='contact'),
]
