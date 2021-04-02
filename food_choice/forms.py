"""Create the forms of the application."""

from django import forms


class NavResearchForm(forms.Form):
    user_research = forms.CharField(
        max_length=50,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Votre aliment",
                "type": "text",
                "name": "nav_search",
                "id": "nav_search",
                "class": "rounded autocomplete_search",
                "size": "25",
            }
        ),
    )


class HomeResearchForm(forms.Form):
    user_research = forms.CharField(
        max_length=50,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Votre aliment",
                "type": "text",
                "name": "home_search",
                "id": "home_search",
                "class": "rounded autocomplete_search",
                "size": "30",
                "autofocus": "autofocus",
            }
        ),
    )
