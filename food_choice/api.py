"""Manage all operations with the OpenFoodFacts API"""

import re
from datetime import datetime

import requests
from colorama import Fore, Style
from progress.bar import Bar


class API:
    """Import products from OpenFoodFact's API"""

    def __init__(self):
        self.products_key = "products"
        self.products_url = "https://fr.openfoodfacts.org/cgi/search.pl?"
        self.products_name_field = "nutrition_grades"
        self.categories_url = "https://fr.openfoodfacts.org/categories.json"
        self.categories_key = "tags"
        self.categories_name_field = "name"
        self.categories_regex = "^[A-Z].+"

    def get_categories(self, nb_cat_selected):
        """Import and return a selection of x categories"""
        date = datetime.now()
        headers = {
            "date": date.__str__()[:19],
            "user-agent": "PurBeurre/0.0.1",
        }

        response = requests.get(self.categories_url, headers=headers, timeout=10)

        category_list = None

        if response.status_code == 200:
            content = response.json()
            imported_categories = content.get(self.categories_key)

            # keep only a selection of x categories capitalized
            category_list = [
                imported_category[self.categories_name_field]
                for imported_category in imported_categories
                if re.fullmatch(
                    self.categories_regex,
                    imported_category[self.categories_name_field],
                )
                is not None
            ]
        else:
            err = f"The error : '{response.status_code}' occurred"
            print(err)

        return category_list[:nb_cat_selected]

    def get_products(self, selected_categories):
        """Import and return a selection of products by category"""
        products = []

        print(Fore.GREEN)
        print(
            "\n-----> Importation des données depuis"
            " l'API d'Open Food Facts <-----\n"
        )
        with Bar("Progression", max=len(selected_categories)) as progress_bar:
            for category in selected_categories:

                payload = {
                    "action": "process",
                    "tagtype_0": "categories",
                    "tag_contains_0": "contains",
                    "tag_0": "category",
                    "sort_by": "last_modified_t",
                    "page_size": "125",
                    "json": "true",
                }

                payload["tag_0"] = f"'{str(category)}''"

                date = datetime.now()
                headers = {
                    "date": date.__str__()[:19],
                    "user-agent": "PurBeurre/0.0.1",
                }

                response = requests.get(
                    self.products_url,
                    params=payload,
                    headers=headers,
                    timeout=10,
                )

                if response.status_code == 200:
                    content = response.json()
                    products.extend(content.get(self.products_key))
                else:
                    err = f"L'erreur : '{response.status_code}' est survenue"
                    print(err)

                progress_bar.next()

        print(f"\n----> {len(products)} produits importés <----")
        print(Style.RESET_ALL)

        return products
