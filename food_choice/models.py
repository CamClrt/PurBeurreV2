"""Models used by the application."""

from django.db import models
from django.utils import timezone

from users.models import User


class Category(models.Model):
    """Represente the categories of a product"""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    """Represente a product"""

    name = models.CharField(max_length=150, null=True)
    code = models.CharField(max_length=13, unique=True)
    brand = models.CharField(max_length=100, null=True)
    photo_url = models.TextField(null=True)
    product_url = models.TextField(null=True)
    nutrition_grade = models.CharField(max_length=1)
    energy_100g = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    saturates = models.IntegerField(default=0)
    carbohydrate = models.IntegerField(default=0)
    sugars = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fiber = models.IntegerField(default=0)
    salt = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, related_name="product")

    def __str__(self):
        return f"{self.name}, {self.code}, {self.nutrition_grade}"


class Favoris(models.Model):
    """Represente the user's favorites products"""

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="favorite_product"
    )
    substitute = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="favorite_substitute"
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorite_owner"
    )
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product", "substitute", "owner"],
                name="unique_user_favoris",
            )
        ]

    def __str__(self):
        return f"{self.owner}: {self.substitute} substitute {self.product}"
