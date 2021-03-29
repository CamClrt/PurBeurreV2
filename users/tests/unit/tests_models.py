from django.test import RequestFactory
from django.test import TestCase

from users.models import Diet
from users.models import Profile
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

        self.diet = Diet.objects.create(diet=Diet.OMNIVOR_DIET)
        self.profile = Profile.objects.create(user=self.user, diet=self.diet)

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

    def test_diet_str(self):
        self.assertEqual(str(self.diet), "1: omnivore")

    def test_profile_str(self):
        self.assertEqual(str(self.profile), "inconnu Profile")
