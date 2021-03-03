from django.test import Client, TestCase
from django.urls import reverse

from food_choice.models import Product
from users.models import User


class TestFavoritesView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="inconnu",
            email="inconnu@gmail.com",
            password="1234AZERTY",
        )
        self.client.login(
            email="inconnu@gmail.com",
            password="1234AZERTY",
        )

    def test_display_favorite_page(self):
        response = self.client.get(reverse("food_choice:favorites"))
        self.assertTemplateUsed(response, "food_choice/favorites.html")
        self.assertEqual(response.status_code, 200)


class TestProductView(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name="Nutella",
            code="1234567890123",
            brand="Ferrero",
            nutrition_grade="e",
        )

    def test_display_product_page(self):
        url = reverse("food_choice:product", args=(self.product.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "food_choice/product.html")


class TestSubstitutesView(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name="Nutella",
            code="1234567890123",
            brand="Ferrero",
            nutrition_grade="e",
        )

    def test_display_substitutes_page(self):
        url = reverse("food_choice:substitutes", args=(self.product.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "food_choice/substitutes.html")


class TestSaveAsfavorisView(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name="Nutella",
            code="1234567890123",
            brand="Ferrero",
            nutrition_grade="e",
        )
        self.substitute = Product.objects.create(
            name="Pâte à tartiner allégée",
            code="6789012345678",
            brand="mamie Bio",
            nutrition_grade="a",
        )

    def test_save_as_favorite_ok(self):
        url = reverse(
            "food_choice:save_as_favoris",
            args=(
                self.product.id,
                self.substitute.id,
            ),
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
