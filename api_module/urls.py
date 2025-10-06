from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductListApiView.as_view()),
    path('check-token/', CheckToken.as_view()),
    path('<int:pk>/', ProductDetailApiView.as_view()),
    path('add/', ProductAddApiView.as_view()),
    path('edit/<str:pk>/', ProductEditApiView.as_view()),
    path('delete/<str:pk>/', ProductDeleteApiView.as_view()),
]