from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView, DeleteView, CreateView


class ArticleHome(ListView):
    model = Article
    template_name = 'TAIApp/index.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home page'
        return context

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


def about(request):
    context = {
        'title': 'About site'
    }
    return render(request, 'TAIApp/about.html', context)


class CreateArticle(CreateView):
    form_class = ArticleForm
    template_name = 'TAIApp/create_article.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create article'
        return context


def sign_in(request):
    return HttpResponse('sign_in')


class ShowArticle(DeleteView):
    model = Article
    template_name = 'TAIApp/article.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'
