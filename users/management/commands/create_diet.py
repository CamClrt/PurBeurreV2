"""Launche the filling of the database on the command line."""

from django.core.management.base import BaseCommand
from progress.bar import Bar

from users.models import Diet


class Command(BaseCommand):
    help = "Create diet in database"

    def handle(self, *args, **kwargs):
        print("\n----> Insertion des données en base <----\n")

        with Bar("Progression", max=len(Diet.DIET_CHOICES)) as bar:
            for diet in range(1, len(Diet.DIET_CHOICES) + 1):
                Diet.objects.create(diet=diet)
                bar.next()
        return
