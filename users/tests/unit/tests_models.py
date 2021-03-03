from django.test import RequestFactory, TestCase

from users.models import User


class TestModels(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="inconnu",
            email="inconnu@email.com",
            password="1234AZERTY",
        )

        self.superuser = User.objects.create_superuser(
            username="superinconnu",
            email="superinconnu@email.com",
            password="1234AZERTY",
        )

    def test_user_str(self):
        self.assertEqual(str(self.user), "inconnu@email.com")

    def test_user_has_perm(self):
        self.assertIs(self.user.has_perm("fake permission"), True)

    def test_user_has_module_perms(self):
        self.assertIs(self.user.has_module_perms("fake app_label"), True)

    def test_simple_user_not_admin_str(self):
        self.assertIs(self.user.is_admin, False)

    def test_superuser_is_admin_str(self):
        self.assertIs(self.superuser.is_admin, True)
