"""Launche the filling of the database on the command line."""

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from progress.bar import Bar

from food_choice.api import API
from food_choice.models import Category, Product


class Command(BaseCommand):
    help = "From OpenFoodFacts API upload product informations in database"

    def handle(self, *args, **kwargs):
        api = API()
        imported_categories = api.get_categories(15)
        imported_products = api.get_products(imported_categories)

        if imported_products is not None:
            self.stdout.write(self.style.SUCCESS("API import: success"))
        else:
            self.stdout.write(self.style.ERROR("API import: error"))

        # insert data in DB
        print("\n----> Insertion des données en base <----\n")

        with Bar("Progression", max=len(imported_products)) as bar:
            for imported_product in imported_products:

                # filter & insert products
                name = imported_product.get("product_name_fr", "")[:150].strip()
                brand = imported_product.get("brands", "")[:100].strip()
                url = imported_product.get("url", "").strip()
                image_url = imported_product.get("image_url", "").strip()
                code = imported_product.get("code", "")[:13].strip()
                nutrition_grade = imported_product.get("nutrition_grades", "")[:1]

                nutriments_list = [
                    "energy_100g",
                    "fat_100g",
                    "saturated_100g",
                    "carbohydrates_100g",
                    "sugars_100g",
                    "proteins_100g",
                    "salt_100g",
                    "fiber_100g",
                ]

                nutriments_dic = {}

                for nutriment in nutriments_list:
                    imported_value = imported_product.get("nutriments", 0).get(
                        nutriment, 0
                    )
                    if isinstance(imported_value, int) is True:
                        value = imported_value
                    else:
                        value = 0
                    nutriments_dic[nutriment] = value

                # insert product in DB
                product_obj = Product(
                    name=name.lower(),
                    code=code,
                    brand=brand,
                    photo_url=image_url,
                    product_url=url,
                    nutrition_grade=nutrition_grade.upper(),
                    energy_100g=nutriments_dic.get("energy_100g", 0),
                    fat=nutriments_dic.get("fat_100g", 0),
                    saturates=nutriments_dic.get("saturates_100g", 0),
                    carbohydrate=nutriments_dic.get("carbohydrate_100g", 0),
                    sugars=nutriments_dic.get("sugars_100g", 0),
                    protein=nutriments_dic.get("protein_100g", 0),
                    fiber=nutriments_dic.get("fiber_100g", 0),
                    salt=nutriments_dic.get("salt_100g", 0),
                )

                try:
                    product_obj.save()

                    # filter & insert categories
                    tmp_categories = imported_product.get("categories", "").split(",")
                    for tmp_category in tmp_categories:
                        if tmp_category is not None:
                            category_name = tmp_category[:50].strip()
                            category_obj = Category(name=category_name)
                            try:
                                category_obj.save()
                            except IntegrityError:
                                category_obj = Category.objects.get(name=category_name)

                except IntegrityError:
                    continue

                bar.next()
        return
