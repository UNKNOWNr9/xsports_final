from django.views.generic import TemplateView


class ArticleListView(TemplateView):
    template_name = 'blog_module/article.html'
