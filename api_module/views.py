
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView

from blog_module.models import Article
from .serializers import ArticleSerializer


class ArticleListApiView(ListAPIView):
    queryset = Article.objects.filter(status='PB')
    serializer_class = ArticleSerializer


class ArticleDetailApiView(RetrieveAPIView):
    queryset = Article.objects.filter(status='PB')
    serializer_class = ArticleSerializer


class ArticleCreateApiView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDeleteApiView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer