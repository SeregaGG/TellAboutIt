from django.shortcuts import render
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
    return HttpResponse('create_article')


def sign_in(request):
    return HttpResponse('sign_in')


def show_article(request, article_id):
    return HttpResponse(f'show_article {article_id}')
