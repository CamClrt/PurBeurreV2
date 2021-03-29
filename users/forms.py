"""Customize the forms of the application."""

from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile
from users.models import User


class UserRegisterForm(UserCreationForm):
    """Customize register formulaire"""

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "john.doe@email.com",
            }
        ),
    )
    username = forms.CharField(
        label="Nom de l'utilisateur",
        widget=forms.TextInput(
            attrs={
                "placeholder": "John Doe",
            }
        ),
    )

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Mot de passe",
                "type": "password",
            }
        ),
    )

    password2 = forms.CharField(
        label="Confirmation de votre mot de passe",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Confirmation",
                "type": "password",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(label="Nom de l'utilisateur")

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]


class DietForm(forms.Form):
    DIET_CHOICES = [
        (1, "omnivore"),
        (2, "flexitarien"),
        (3, "végétarien"),
        (4, "végétalien"),
        (5, "crudivor"),
    ]
    diet = forms.ChoiceField(
        label="Régime alimentaire",
        choices=DIET_CHOICES,
    )
