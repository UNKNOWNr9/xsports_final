from django.views.generic import TemplateView


class ProductListView(TemplateView):
    template_name = 'shop_module/product_list.html'
