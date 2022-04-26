from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


def home_page(request):
    articles = Article.objects.all()
    context = {
        'title': 'Home page',
        'articles': articles
    }
    return render(request, 'TAIApp/index.html', context)


def about(request):
    context = {
        'title': 'About site'
    }
    return render(request, 'TAIApp/about.html', context)


def create_article(request):
    context = {
        'title': 'Create article'
    }
    return render(request, 'TAIApp/create_article.html', context)


def sign_in(request):
    return HttpResponse('sign_in')


def show_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article
    }
    return render(request, 'TAIApp/article.html', context)
