from django.test import TestCase
from product.models import Product

class ProductModelTest(TestCase):
    def test_criacao_produto(self):
        produto = Product.objects.create(title='livro', price=30)
        self.assertEqual(produto.title, 'livro')
        self.assertEqual(produto.price, 30)
