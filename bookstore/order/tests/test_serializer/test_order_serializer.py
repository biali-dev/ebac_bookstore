from django.test import TestCase
from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory, OrderFactory
from order.serializers import OrderSerializer
from order.models import Order


class TestOrderSerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(title='tech')
        self.product1 = ProductFactory(title='mouse', price=100, category=[self.category])
        self.product2 = ProductFactory(title='keyboard', price=200, category=[self.category])
        self.user = UserFactory()

    def test_create_order_serializer(self):
        """Testa se o serializer cria corretamente um pedido"""
        data = {
            "products_id": [self.product1.id, self.product2.id],
            "user": self.user.id
        }

        serializer = OrderSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        order = serializer.save()

        # Verifica se o pedido foi criado corretamente
        self.assertIsInstance(order, Order)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.product.count(), 2)
        self.assertIn(self.product1, order.product.all())
        self.assertIn(self.product2, order.product.all())

    def test_get_total(self):
        """Testa se o campo 'total' retorna a soma correta dos preços"""
        order = OrderFactory(user=self.user, product=[self.product1, self.product2])
        serializer = OrderSerializer(order)

        expected_total = float(self.product1.price + self.product2.price)
        self.assertEqual(serializer.data["total"], expected_total)

    def test_serializer_output_fields(self):
        """Garante que o serializer retorna os campos esperados"""
        order = OrderFactory(user=self.user, product=[self.product1])
        serializer = OrderSerializer(order)

        data = serializer.data
        self.assertIn("product", data)
        self.assertIn("total", data)
        self.assertIn("user", data)
        self.assertIn("products_id", serializer.fields)
