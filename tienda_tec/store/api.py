from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer

        return self.serializer_class
