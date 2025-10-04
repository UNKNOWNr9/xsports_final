from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from .models import Products


class ProductApiView(APIView):
    def get(self, request):
        query = Products.objects.all()
        serializer = ProductSerializer(instance=query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'response': 'added'})
        return Response(serializer.errors)


class ProductDetailApiView(APIView):
    def get(self, request, pk):
        query = Products.objects.get(pk=pk)
        serializer = ProductSerializer(instance=query)
        return Response(serializer.data)