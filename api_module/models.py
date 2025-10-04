from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    content = models.TextField(verbose_name='توضیحات')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'محصولات 2'
        verbose_name_plural = 'محصولات 2'

    def __str__(self):
        return self.title
