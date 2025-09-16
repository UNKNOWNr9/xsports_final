from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article, ArticleCategory
from django.db.models import Count


class ArticleListView(ListView):
    template_name = 'blog_module/article_list.html'
    queryset = Article.objects.published().order_by('-created_at')
    paginate_by = 3
    context_object_name = 'articles'


class ArticleDetail(DetailView):
    template_name = 'blog_module/article_detail.html'
    queryset = Article.objects.published()
    context_object_name = 'article'


def article_sidebar(request):
    categories = ArticleCategory.objects.filter(is_active=True).annotate(count=Count('articles'))
    context = {
        'categories': categories
    }
    return render(request, 'shared/includes/sidebar.html', context)


def article_by_category(request, slug):
    category = get_object_or_404(ArticleCategory, slug=slug, is_active=True)
    articles = category.articles.published().order_by('-created_at')
    context = {
        'articles': articles
    }
    return render(request, 'blog_module/category_detail.html', context)
