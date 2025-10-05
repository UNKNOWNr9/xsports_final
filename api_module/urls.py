from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductListApiView.as_view()),
    path('<int:pk>/', ProductDetailApiView.as_view()),
    path('add/', ProductAddApiView.as_view()),
]