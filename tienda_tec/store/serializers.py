from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price',
                  'stock', 'created', 'updated']
        read_only_fields = ['created', 'updated', 'id']


class ProductDetailSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ['id']


class ProductParameterSerializer(serializers.Serializer):
    parameters = serializers.JSONField()
