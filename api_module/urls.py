from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleListApiView.as_view()),
    path('<int:pk>/', ArticleDetailApiView.as_view()),
    path('create/', ArticleCreateApiView.as_view()),
    path('delete/<int:pk>/', ArticleDeleteApiView.as_view()),
    ]