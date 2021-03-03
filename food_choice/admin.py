"""Customize the administration part of the application."""

from django.contrib import admin

from .models import Category, Favoris, Product

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Favoris)
