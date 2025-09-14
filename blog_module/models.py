from django.db import models
from .managers import ArticleManager
from django.urls import reverse
from account_module.models import CustomUser


class ArticleCategory(models.Model):
    title = models.CharField(max_length=25, unique=True, verbose_name='عنوان')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    slug = models.SlugField(max_length=25, unique=True, verbose_name='آدرس')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Article(models.Model):
    class STATUS(models.TextChoices):
        PUBLISHED = 'PB', 'منتشر شده'
        DRAFT = 'DF', 'پیشنویس'
        INVESTIGATION = 'IN', 'درحال بررسی'
        REJECTED = 'RJ', 'رد شده'

    title = models.CharField(max_length=50, verbose_name='عنوان')
    body = models.TextField(verbose_name='متن مقاله')
    image = models.ImageField(upload_to='article', verbose_name='تصویر')  ###
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='نویسنده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ اپدیت')
    status = models.CharField(max_length=25, choices=STATUS.choices, default=STATUS.DRAFT, verbose_name='وضعیت')
    rejected_reason = models.TextField(blank=True, null=True, verbose_name='علت رد شدن')
    slug = models.SlugField(max_length=50, unique=True, blank=True, editable=False, verbose_name='آدرس')
    category = models.ManyToManyField(ArticleCategory, verbose_name='دسته بندی')
    objects = ArticleManager()

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = self.title.replace(' ', '+')
            slug = base_slug
            counter = 1
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
