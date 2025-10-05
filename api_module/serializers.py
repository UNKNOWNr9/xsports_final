from rest_framework import serializers
from .models import Products


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='آیدی', required=False)
    title = serializers.CharField(max_length=100, label='عنوان')
    content = serializers.CharField(max_length=3000, label='توضیحات')
    is_active = serializers.BooleanField(default=False, label='فعال / غیرفعال', required=False)

    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('body', instance.content)
        instance.save()
        return instance