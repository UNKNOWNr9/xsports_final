from django.contrib import admin
from .models import Article, ArticleCategory


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at', 'slug', 'category', 'status']
