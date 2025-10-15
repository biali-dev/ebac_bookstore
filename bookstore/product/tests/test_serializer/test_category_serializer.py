from django.test import TestCase
from product.serializers.category_serializer import CategorySerializers
from product.models import Category


class TestCategorySerializer(TestCase):

    def test_create_category_serializer(self):
        """Testa se o serializer cria corretamente uma categoria"""
        data = {
            "title": "Eletrônicos",
            "description": "Categoria de produtos tecnológicos",
            "active": True
        }

        serializer = CategorySerializers(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        category = serializer.save()

        # Verificações
        self.assertIsInstance(category, Category)
        self.assertEqual(category.title, data["title"])
        self.assertEqual(category.description, data["description"])
        self.assertTrue(category.active)
        # slug é opcional e pode ser gerado automaticamente no modelo
        self.assertTrue(hasattr(category, "slug"))

    def test_serializer_output_fields(self):
        """Garante que o serializer retorna os campos esperados"""
        category = Category.objects.create(
            title="Acessórios",
            description="Itens complementares",
            active=True
        )

        serializer = CategorySerializers(category)
        data = serializer.data

        expected_fields = {"title", "slug", "description", "active"}
        self.assertTrue(expected_fields.issubset(set(data.keys())))
        self.assertEqual(data["title"], category.title)
        self.assertEqual(data["description"], category.description)

    def test_invalid_serializer(self):
        """Testa caso inválido — sem título"""
        data = {
            "description": "Sem título",
            "active": True
        }

        serializer = CategorySerializers(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)
