from django.urls import path
from .views import ProductListView, ProductDetailView, ProductByCategory

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('category/<str:slug>/', ProductByCategory.as_view(), name='product_by_category'),
    # exceptions
    path('<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
