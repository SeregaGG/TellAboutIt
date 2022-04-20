from TAIApp import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about, name='about'),
    path('create_article/', views.create_article, name='create_article'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('article/<int:article_id>', views.show_article, name='show_article'),
]