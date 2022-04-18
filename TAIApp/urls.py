from TAIApp import views
from django.urls import path

urlpatterns = [
    path('articles/', views.articles),
    path('', views.home_page),
]