from rest_framework import serializers
from .models import Products


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, label='عنوان')
    content = serializers.CharField(label='توضیحات')
    is_active = serializers.BooleanField(label='فعال / غیرفعال')

    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    def __str__(self):
        return self.title
