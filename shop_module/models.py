from django.db import models
from django.utils.html import format_html

from .managers import ProductManager


class Color(models.Model):
    title = models.CharField(max_length=20, verbose_name='عنوان')

    class Meta:
        verbose_name = 'رنگ بندی'
        verbose_name_plural = 'رنگ بندی ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام محصول')
    body = models.TextField(verbose_name='توضیحات محصولات')
    slug = models.SlugField(max_length=50, unique=True, blank=True, editable=False, verbose_name='آدرس')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to='products', verbose_name='تصویر')
    color = models.ManyToManyField(Color, related_name='products', verbose_name='رنگ')
    discount = models.PositiveSmallIntegerField(default=0, verbose_name='تخفیف')
    stock = models.PositiveIntegerField(default=0, verbose_name='موجودی')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت')
    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = self.title.replace(' ', '+')
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def image_tag(self):
        if self.image:
            return format_html('<img src="{}" width="100" />', self.image.url)
        return "—"

    image_tag.short_description = "تصویر"
