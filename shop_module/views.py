from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.published()
    template_name = 'shop_module/product_list.html'
    paginate_by = 1
    context_object_name = 'products'


class ProductDetailView(DetailView):
    queryset = Product.objects.published()
    template_name = 'shop_module/product_detail.html'
    context_object_name = 'product'
