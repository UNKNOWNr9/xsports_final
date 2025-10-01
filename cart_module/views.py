# cart_module/views.py
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from shop_module.models import Product
from .models import Cart, CartItem


class AddToCartView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        cart, created = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += 1
            item.save()
        return redirect("cart")


class DeleteFromCartView(View):
    def post(self, request, pk):
        cart = get_object_or_404(Cart, user=request.user)
        item = get_object_or_404(CartItem, cart=cart, pk=pk)
        item.delete()
        return redirect('cart')


class UpdateQuantityView(View):
    def post(self, request, pk):
        cart = get_object_or_404(Cart, user=request.user)
        item = get_object_or_404(CartItem, cart=cart, pk=pk)
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()
        return redirect("cart")



class CartView(View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        return render(request, "cart_module/cart_detail.html", {"cart": cart})
