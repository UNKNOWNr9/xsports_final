from django.contrib import admin

from .models import Color, Product, ProductKeyFeatures


class ProductKeyFeaturesInline(admin.TabularInline):
    model = ProductKeyFeatures
    extra = 1
    min_num = 0
    can_delete = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductKeyFeaturesInline]
    list_display = ['title', 'image_tag', 'slug', 'price', 'created_at', 'updated_at', 'is_active', 'stock']
    list_filter = ['created_at', 'is_active', 'stock']
    search_fields = ['title', 'body', 'slug', 'price']
