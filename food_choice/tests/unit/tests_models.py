from django.db import IntegrityError
from django.test import TestCase

from food_choice.models import Category, Favoris, Product
from users.models import User


class TestModels(TestCase):
    def test_product_str(self):
        product = Product.objects.create(
            name="Nutella",
            code="1234567890123",
            brand="Ferrero",
            photo_url="https://fr.openfoodfacts.org/produit/26073651/nutella",  # noqa: E501
            product_url="https://static.openfoodfacts.org/images/products/26073651/nutella_img.jpg",  # noqa: E501
            nutrition_grade="e",
            energy_100g=1000,
            fat=500,
            saturates=500,
            carbohydrate=500,
            sugars=500,
            protein=500,
            fiber=500,
            salt=500,
        )
        self.assertEqual(str(product), "Nutella, 1234567890123, e")

    def test_category_str(self):
        category = Category.objects.create(
            name="petit-déjeuner",
        )
        self.assertEqual(str(category), "petit-déjeuner")

    def test_product_has_categories(self):
        product = Product.objects.create(
            name="Nutella",
            code="1234567890123",
            brand="Ferrero",
            nutrition_grade="e",
        )
        cat1 = Category.objects.create(name="goûter")
        cat2 = Category.objects.create(name="petit-déjeuner")
        product.categories.set([cat1.pk, cat2.pk])
        self.assertEqual(product.categories.count(), 2)

    def test_favorite_str(self):
        product = Product.objects.create(
            name="Nutella",
            code="1234567890123",
            brand="Ferrero",
            nutrition_grade="e",
        )
        substitute = Product.objects.create(
            name="Pâte à tartiner allégée",
            code="6789012345678",
            brand="mamie Bio",
            nutrition_grade="a",
        )
        user = User.objects.create_user(
            username="inconnu",
            email="inconnu@gmail.com",
            password="1234AZERTY",
        )

        favoris = Favoris(product=product, substitute=substitute, owner=user)
        self.assertEqual(
            str(favoris),
            "inconnu@gmail.com: Pâte à tartiner allégée, 6789012345678, a substitute Nutella, 1234567890123, e",  # noqa: E501
        )

    def test_favorite_unique_constraint(self):
        product = Product.objects.create(
            name="Nutella",
            code="1234567890123",
            brand="Ferrero",
            nutrition_grade="e",
        )
        substitute = Product.objects.create(
            name="Pâte à tartiner allégée",
            code="6789012345678",
            brand="mamie Bio",
            nutrition_grade="a",
        )
        user = User.objects.create_user(
            username="inconnu",
            email="inconnu@gmail.com",
            password="1234AZERTY",
        )

        Favoris(product=product, substitute=substitute, owner=user)

        message = 'duplicate key value violates unique constraint "food_choice_product_code_key"'  # noqa: E501
        with self.assertRaisesMessage(IntegrityError, message):
            product = Product.objects.create(
                name="Nutella",
                code="1234567890123",
                brand="Ferrero",
                nutrition_grade="e",
            )
            substitute = Product.objects.create(
                name="Pâte à tartiner allégée",
                code="6789012345678",
                brand="mamie Bio",
                nutrition_grade="a",
            )
            user = User.objects.create_user(
                username="inconnu",
                email="inconnu@gmail.com",
                password="1234AZERTY",
            )

            Favoris(product=product, substitute=substitute, owner=user)
