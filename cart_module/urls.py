from django.urls import path
from .views import CartView, AddToCart, RemoveFromCart, UpdateCart

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:pk>/', AddToCart.as_view(), name='add_to_cart'),
    path('remove/<int:pk>/', RemoveFromCart.as_view(), name='remove_from_cart'),
    path('update/<int:pk>/', UpdateCart.as_view(), name='update_cart'),
]
