from django.test import TestCase
from product.factories import CategoryFactory, ProductFactory
from product.serializers.product_serializer import ProductSerializers
from product.models import Product


class TestProductSerializer(TestCase):

    def setUp(self):
        self.category1 = CategoryFactory(title='tech')
        self.category2 = CategoryFactory(title='home')

    def test_create_product_serializer(self):
        """Testa se o serializer cria corretamente um produto com categorias"""
        data = {
            "title": "Mouse Gamer",
            "description": "Mouse óptico de alta precisão",
            "price": 150.0,
            "active": True,
            "categories_id": [self.category1.id, self.category2.id],
        }

        serializer = ProductSerializers(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        product = serializer.save()

        # Verificações
        self.assertIsInstance(product, Product)
        self.assertEqual(product.title, data["title"])
        self.assertEqual(product.price, data["price"])
        self.assertTrue(product.active)
        self.assertEqual(product.category.count(), 2)
        self.assertIn(self.category1, product.category.all())
        self.assertIn(self.category2, product.category.all())

    def test_serializer_output_fields(self):
        """Garante que o serializer retorna os campos esperados"""
        product = ProductFactory(category=[self.category1])
        serializer = ProductSerializers(product)

        data = serializer.data
        expected_fields = {"id", "title", "description", "price", "active", "category", "categories_id"}
        self.assertTrue(expected_fields.issubset(set(serializer.fields.keys())))
        self.assertEqual(data["category"][0]["title"], self.category1.title)

    def test_invalid_serializer(self):
        """Testa caso inválido — sem título"""
        data = {
            "description": "Sem título",
            "price": 50,
            "active": True,
            "categories_id": [self.category1.id],
        }

        serializer = ProductSerializers(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)
