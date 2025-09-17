from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from account_module.models import CustomUser
from .models import Article, ArticleCategory


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


class ArticleByCategory(ListView):
    template_name = 'blog_module/article_by_category.html'
    paginate_by = 3
    context_object_name = 'articles'

    def get_queryset(self):
        self.category = get_object_or_404(
            ArticleCategory, slug=self.kwargs['slug'], is_active=True
        )
        return self.category.articles.published().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ArticleByAuthor(ListView):
    template_name = 'blog_module/article_by_author.html'
    paginate_by = 3
    context_object_name = 'articles'

    def get_queryset(self):
        self.author = get_object_or_404(CustomUser, username=self.kwargs['username'])
        return (
            Article.objects.published()
            .filter(author=self.author)
            .select_related('author')
            .order_by('-created_at')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context