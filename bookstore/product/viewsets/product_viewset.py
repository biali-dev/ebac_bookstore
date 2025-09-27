from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializer import ProductSerializers

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializers
    
    def get_queryset(self):
        return Product.objects.all()
    