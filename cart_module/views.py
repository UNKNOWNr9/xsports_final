from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from shop_module.models import Product


class CartView(View):
    def get(self, request):
        cart = request.session.get("cart", {})
        products = []
        total_price = 0

        for product_id, item in cart.items():
            product = get_object_or_404(Product, id=product_id)
            quantity = item["quantity"]
            price = product.price * quantity
            products.append({
                "product": product,
                "quantity": quantity,
                "total": price
            })
            total_price += price

        return render(request, 'cart_module/cart_detail.html', {
            "products": products,
            "total_price": total_price
        })


class AddToCart(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        cart = request.session.get("cart", {})

        if str(pk) in cart:
            cart[str(pk)]["quantity"] += 1
        else:
            cart[str(pk)] = {"quantity": 1}

        request.session["cart"] = cart
        return redirect('cart')


class RemoveFromCart(View):
    def post(self, request, pk):
        cart = request.session.get("cart", {})
        if str(pk) in cart:
            del cart[str(pk)]
            request.session["cart"] = cart
        return redirect("cart")


class UpdateCart(View):
    def post(self, request, pk):
        quantity = int(request.POST.get("quantity", 1))
        cart = request.session.get("cart", {})
        if str(pk) in cart:
            cart[str(pk)]["quantity"] = quantity
            request.session["cart"] = cart
        return redirect("cart")
