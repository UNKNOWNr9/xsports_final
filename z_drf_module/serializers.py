from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)