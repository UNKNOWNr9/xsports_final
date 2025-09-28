from django.urls import path
from .views import ProductListView, ProductDetailView


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product_detail/<str:slug>/', ProductDetailView.as_view(), name='product_detail')
]