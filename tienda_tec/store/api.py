from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from .api_data import Data
from .models import Product
from rest_framework import status
from .serializers import ProductSerializer, ProductDetailSerializer, ProductParameterSerializer
from rest_framework.response import Response
from django.core.serializers.json import DjangoJSONEncoder
import json


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer

        return self.serializer_class


class ProductServices(APIView):
    def post(self, request):
        serializer = ProductParameterSerializer(data=request.data)
        if serializer.is_valid():
            parameters = serializer.validated_data['parameters']
            dat = Data()
            res = dat.get_products(parameters)
            res2 = json.dumps(list(res.values()), cls=DjangoJSONEncoder)
            return Response({"Resultado": res2}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
