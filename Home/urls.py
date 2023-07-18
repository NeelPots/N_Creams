from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path("", views.index, name='Home'),
    path("Stores", views.Stores, name='Stores'),
    path('More info', views.More_info, name = 'More info' ),
    path('Contact us', views.Contact_us, name = 'Contact us'),
]