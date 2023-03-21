from django.urls import path 
from . import views
from django.contrib import admin

urlpatterns = [
    
    path('form/', views.function, name='form'),
    path('/', views.function, name='form'),
]