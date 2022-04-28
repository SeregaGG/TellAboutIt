from django import forms
from .models import *


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'is_published', 'author_id']  # author_id temporary
