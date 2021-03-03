"""Init context processors."""

from food_choice.forms import NavResearchForm


def search_in_navbar(request):
    return {
        "nav_form": NavSearchForm(),
    }
