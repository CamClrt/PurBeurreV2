"""Views used by the application."""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import DietForm
from .forms import ProfileUpdateForm
from .forms import UserRegisterForm
from .forms import UserUpdateForm
from .models import Diet
from .models import Profile
from .models import User


def register(request):
    """Display a register page and allow users to register"""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"{username}: compte créé, vous pouvez vous connecter !",
            )
            email = form.cleaned_data.get("email")
            user = User.objects.get(email=email)
            diet = Diet.objects.get(diet=1)
            Profile.objects.create(user=user, diet=diet)
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def update_profile(request):
    """Update the profil page when user is logged in"""
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        d_form = DietForm(request.POST)
        if u_form.is_valid() and p_form.is_valid() and d_form.is_valid:
            u_form.save()
            p_form.save()
            diet = Diet.objects.get(diet=request.POST["diet"])
            profile.diet = diet
            profile.save()
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=profile)
        d_form = DietForm()

    context = {
        "u_form": u_form,
        "p_form": p_form,
        "d_form": d_form,
        "profile": profile,
    }

    return render(request, "users/update_profile.html", context)


@login_required
def profile(request):
    """Display the profil page when user is logged in"""
    profile = Profile.objects.get(user=request.user)
    context = {"profile": profile}
    return render(request, "users/profile.html", context)
