from django.test import Client, TestCase
from django.urls import reverse

from users.models import User


class TestRegisterView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registration_ok(self):
        data = {
            "username": "inconnu",
            "email": "inconnu@gmail.com",
            "password1": "1234AZERTY",
            "password2": "1234AZERTY",
        }

        response = self.client.post(reverse("register"), data)
        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, "/login/")


class TestProfileView(TestCase):
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

    def test_display_profile_page_ok(self):
        response = self.client.get(reverse("profile"))
        self.assertTemplateUsed(response, "users/profile.html")
        self.assertEqual(response.status_code, 200)
