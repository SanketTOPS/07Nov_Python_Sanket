from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('profile/',views.profile),
   path('notes/',views.notes),
   path('about/',views.about),
   path('contact/',views.contact),
]
