from django.test import TestCase

from users.models import User


class TestModels(TestCase):
    def test_create_simple_user_without_email(self):
        message = "Users must have an email address"
        with self.assertRaisesMessage(ValueError, message):
            User.objects.create_user(
                username="inconnu",
                email="",
                password="1234AZERTY",
            )

    def test_simple_user_not_admin_str(self):
        user = User.objects.create_user(
            username="inconnu",
            email="inconnu@gmail.com",
            password="1234AZERTY",
        )
        self.assertIs(user.is_admin, False)

    def test_superuser_is_admin_str(self):
        superuser = User.objects.create_superuser(
            username="inconnu",
            email="inconnu@gmail.com",
            password="1234AZERTY",
        )
        self.assertIs(superuser.is_admin, True)
