from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def articles(request):
    Article
    return HttpResponse('<h1>Temp resp<h1>')


def home_page(request):
    return HttpResponse('<h1>Home page.<h1>')