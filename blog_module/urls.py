from django.urls import path
from .views import ArticleListView, ArticleDetail, ArticleByCategory, ArticleByAuthor

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('category/<slug:slug>/', ArticleByCategory.as_view(), name='article_by_category'),
    path('author/<str:username>/', ArticleByAuthor.as_view(), name='article_by_author'),
    path('<str:slug>/', ArticleDetail.as_view(), name='article_detail'),
]