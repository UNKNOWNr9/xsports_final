from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView

from .forms import ProductCommentForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = ProductCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'برای ارسال نظر باید اول وارد حساب کاربری شوید.')
            return redirect(request.path)
        self.object = self.get_object()

        product_comment_form = ProductCommentForm(request.POST)
        if product_comment_form.is_valid():
            comment = product_comment_form.save(commit=False)
            comment.product = self.object
            comment.author = request.user
            comment.save()
            messages.success(request, 'کامنت شما ثبت شد، طی 48 ساعت پس از تایید نمایش داده میشود.')
        context = self.get_context_data()
        context['comment_form'] = product_comment_form
        return redirect(self.request.path_info)

