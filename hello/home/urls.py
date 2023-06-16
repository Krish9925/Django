from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("video", views.video, name='video'),
    path("blog", views.blog, name='blog'),
    path("portfolio", views.portfolio, name='portfolio'),
    path("contact", views.contact, name='contact'),
    
]