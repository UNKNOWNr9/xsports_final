from django.urls import path
from .views import ArticleListApiView, ArticleDetailApiView

urlpatterns = [
    path('', ArticleListApiView.as_view()),
    path('<int:pk>/', ArticleDetailApiView.as_view()),
    path('create/<int:pk>/', ArticleDetailApiView.as_view()),
    path('delete/<int:pk>/', ArticleDetailApiView.as_view()),
    ]