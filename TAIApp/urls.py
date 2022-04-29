from TAIApp import views
from django.urls import path

urlpatterns = [
    path('', views.ArticleHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('create_article/', views.CreateArticle.as_view(), name='create_article'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('article/<int:article_id>', views.ShowArticle.as_view(), name='show_article'),
]