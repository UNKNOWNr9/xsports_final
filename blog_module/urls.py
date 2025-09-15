from django.urls import path
from .views import ArticleListView, ArticleDetail

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<str:slug>/', ArticleDetail.as_view(), name='article_detail'),
]