from django.contrib import admin

from .models import Color, Product


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    list_filter = ['title', ]
    search_fields = ['title', ]



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'slug', 'price', 'created_at', 'updated_at', 'is_active', 'stock']
    list_filter = ['created_at', 'is_active', 'stock']
    search_fields = ['title', 'body', 'slug', 'price']