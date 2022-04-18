from TAIApp import views
from django.urls import path

urlpatterns = [
    path('', views.home_page),
    path('about/', views.about),
]