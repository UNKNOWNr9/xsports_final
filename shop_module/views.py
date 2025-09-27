from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.published()
    template_name = 'shop_module/product_list.html'
    paginate_by = 12
    context_object_name = 'products'
