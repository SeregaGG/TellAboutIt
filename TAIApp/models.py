from django.db import models
from django.db.models import Model
from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('show_article', kwargs={'article_id': self.pk})
