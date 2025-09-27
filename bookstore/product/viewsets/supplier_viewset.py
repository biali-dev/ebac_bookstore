from rest_framework.viewsets import ModelViewSet
from product.models.supplier import Supplier
from product.serializers.supplier_serializer import SupplierSerializer

class SupplierViewSet(ModelViewSet):
    serializer_class = SupplierSerializer

    def get_queryset(self):
        return Supplier.objects.all()
