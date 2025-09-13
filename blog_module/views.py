from django.views.generic import ListView
from .models import Article


class ArticleListView(ListView):
    template_name = 'blog_module/article_list.html'
    queryset = Article.objects.filter(status='PB')
    paginate_by = 3
    context_object_name = 'articles'
