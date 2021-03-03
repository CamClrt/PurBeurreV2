from django.contrib.auth.models import AnonymousUser
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from users.models import User
from users.views import profile


class TestLoginView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_display_login_page(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")
        self.assertContains(response, "username")
        self.assertContains(response, "password")


class TestLogoutView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_display_logout_page(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/logout.html")


class TestRegisterView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_display_register_page(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/register.html")
        self.assertContains(response, "username")
        self.assertContains(response, "email")
        self.assertContains(response, "password1")
        self.assertContains(response, "password2")


class TestProfileView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="inconnu",
            email="inconnu@gmail.com",
            password="1234AZERTY",
        )

    def test_display_profile_ok(self):
        request = self.factory.get(reverse("profile"))
        request.user = self.user
        response = profile(request)
        self.assertEqual(response.status_code, 200)

    def test_display_profile_not_ok(self):
        request = self.factory.get(reverse("profile"))
        request.user = AnonymousUser()
        response = profile(request)
        self.assertEqual(response.status_code, 302)
