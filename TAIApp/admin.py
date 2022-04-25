from django.contrib import admin
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail')
    list_display_links = ('name',)
    search_fields = ('name', 'mail')


class CustomArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'author_id', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Article, CustomArticleAdmin)
