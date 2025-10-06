from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Products
from .serializers import ProductSerializer
from account_module.permissions import BlockedUserPermission


class ProductListApiView(APIView):
    authentication_classes = [TokenAuthentication]

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


class CheckToken(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'user_hashed_password': user.password,
            'user_email': user.email,
        })
