from .views import *
from django.urls import path


urlpatterns = [
    path('', ProductApiView.as_view()),
    path('<int:pk>/', ProductDetailApiView.as_view()),
]