from django.test import Client
from django.test import TestCase


class TestCompleteView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_use_autocompletion(self):
        response = self.client.get("/autocomplete/?term=nut")
        self.assertEqual(response.status_code, 200)
