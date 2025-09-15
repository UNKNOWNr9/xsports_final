from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Article, ArticleCategory
from django.shortcuts import get_object_or_404


class ArticleListView(ListView):
    template_name = 'blog_module/article_list.html'
    queryset = Article.objects.published()
    paginate_by = 3
    context_object_name = 'articles'


class ArticleDetail(DetailView):
    template_name = 'blog_module/article_detail.html'
    queryset = Article.objects.published()
    context_object_name = 'article'


def article_sidebar(request):
    categories = ArticleCategory.objects.filter(is_active=True)
    context = {
        'categories': categories
    }
    return render(request, 'shared/includes/sidebar.html', context)
