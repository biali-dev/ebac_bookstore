from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from product.models import Product
from product.serializers.product_serializer import ProductSerializers

class ProductViewSet(ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializers
    
    def get_queryset(self):
        return Product.objects.all()
    