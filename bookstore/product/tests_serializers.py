from rest_framework.test import APITestCase
from product.models import Product
from product.serializers import ProductSerializers

class ProdutoSerializerTest(APITestCase):
    def test_produto_serializer(self):
        produto = Product.objects.create(title='livro', price=30)
        serializer = ProductSerializers(produto)
        esperado = {'id': produto.id, 'title': 'livro', 'price': 30}
        self.assertEqual(serializer.data, esperado)