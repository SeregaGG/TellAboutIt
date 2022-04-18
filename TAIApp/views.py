from django.shortcuts import render
from django.http import HttpResponse
from .models import *

menu = ['About site', 'Add article', 'Sign in']


def home_page(request):
    articles = Article.objects.all()
    return render(request, 'TAIApp/index.html', {'title': 'Home page', 'menu': menu, 'articles': articles})


def about(request):
    #userq = User.objects.get(pk=1)
    #newArticle = Article(title='Second article', content='dasfas wqess dsa', author_id=userq)
    #newArticle.save()
    return render(request, 'TAIApp/about.html', {'title': 'About site', 'menu': menu})
