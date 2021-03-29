from django.contrib.auth.models import AnonymousUser
from django.test import Client
from django.test import RequestFactory
from django.test import TestCase
from django.urls import reverse

from food_choice.views import favorites
from users.models import User


class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_display_home_page(self):
        response = self.client.get(reverse("food_choice:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "user_research")


class TestLegalNoticesView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_display_legal_notices_page(self):
        response = self.client.get(reverse("food_choice:legal_notices"))
        self.assertEqual(response.status_code, 200)


class TestFavoritesView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="inconnu3",
            email="inconnu3@gmail.com",
            password="1234AZERTY",
        )

    def test_display_favorites_ok(self):
        request = self.factory.get(reverse("food_choice:favorites"))
        request.user = self.user
        response = favorites(request)
        self.assertEqual(response.status_code, 200)

    def test_display_favorites_not_ok(self):
        request = self.factory.get(reverse("food_choice:favorites"))
        request.user = AnonymousUser()
        response = favorites(request)
        self.assertEqual(response.status_code, 302)


class TestProductsView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_display_products_page(self):
        user_research = {"user_research": "random_product"}
        response = self.client.post(
            reverse("food_choice:products"),
            data=user_research,
        )
        self.assertEqual(response.status_code, 200)
