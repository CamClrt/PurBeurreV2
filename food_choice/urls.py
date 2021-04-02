"""Centralize the application urls"""

from django.urls import path

from . import views


app_name = "food_choice"

urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),
    path(
        "legal_notices/",
        views.legal_notices,
        name="legal_notices",
    ),
    path(
        "product/<int:product_id>/",
        views.product,
        name="product",
    ),
    path(
        "products/",
        views.products,
        name="products",
    ),
    path(
        "substitutes/<int:product_id>/",
        views.substitutes,
        name="substitutes",
    ),
    path(
        "save_as_favoris/<int:product_id>/<int:substitute_id>/",
        views.save_as_favoris,
        name="save_as_favoris",
    ),
    path(
        "delete_favoris/<int:favorite_id>/",
        views.delete_favoris,
        name="delete_favoris",
    ),
    path(
        "favorites/",
        views.favorites,
        name="favorites",
    ),
]
