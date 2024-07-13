   
   
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    #path('',views.blackcoffer, name='blackcoffer'),
    path('',views.index, name='dashboard-index'),
    
]
