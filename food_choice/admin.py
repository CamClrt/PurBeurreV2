"""Customize the administration part of the application."""

from django.contrib import admin

from .models import Category
from .models import Favoris
from .models import Product


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Favoris)
