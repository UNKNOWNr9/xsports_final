from django.urls import path
from .views import ArticleListView, ArticleDetail, article_by_category

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('category/<slug:slug>/', article_by_category, name='article_by_category'),
    path('<str:slug>/', ArticleDetail.as_view(), name='article_detail'),
]