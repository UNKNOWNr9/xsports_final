from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products
from .serializers import ProductSerializer


class ProductListApiView(APIView):
    def get(self, request):
        instance = Products.objects.all()
        serializer = ProductSerializer(instance=instance, many=True)
        return Response(serializer.data)


class ProductDetailApiView(APIView):
    def get(self, request, pk):
        instance = Products.objects.get(pk=pk)
        serializer = ProductSerializer(instance=instance)
        return Response(data=serializer.data)


class ProductAddApiView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Response': 'Product Added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class ProductEditApiView(APIView):
    def post(self, request, pk):
        instance = Products.objects.get(pk=pk)
        serializer = ProductSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'response': 'success'})
        return Response(serializer.errors)


class ProductDeleteApiView(APIView):
    def post(self, request, pk):
        instance = Products.objects.get(pk=pk)
        instance.delete()
        return Response({'Response': 'deleted'})
