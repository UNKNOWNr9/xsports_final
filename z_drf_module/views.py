from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
from account_module.models import CustomUser


class HelloView(APIView):
    def get(self, request):
        query = CustomUser.objects.filter(is_active=True)
        api = ProductSerializer(instance=query, many=True)
        return Response(data=api.data)