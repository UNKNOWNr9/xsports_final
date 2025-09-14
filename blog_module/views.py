from django.views.generic import ListView, TemplateView
from .models import Article
from django.shortcuts import render, get_object_or_404


class ArticleListView(ListView):
    template_name = 'blog_module/article_list.html'
    queryset = Article.objects.published()
    paginate_by = 3
    context_object_name = 'articles'