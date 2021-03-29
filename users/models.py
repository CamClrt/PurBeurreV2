"""Models used by the application."""

from PIL import Image
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """Creates and saves a user with his email, username and password"""

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """Creates and saves a superuser his email, username and password"""

        user = self.create_user(
            email,
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=25,
        default="utilisateur",
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin


class Diet(models.Model):
    OMNIVOR_DIET = 1
    FLEXITARIEN_DIET = 2
    VEGETARIEN_DIET = 3
    VEGETALIEN_DIET = 4
    CRUDIVOR_DIET = 5
    DIET_CHOICES = [
        (OMNIVOR_DIET, "omnivore"),
        (FLEXITARIEN_DIET, "flexitarien"),
        (VEGETARIEN_DIET, "végétarien"),
        (VEGETALIEN_DIET, "végétalien"),
        (CRUDIVOR_DIET, "crudivor"),
    ]

    diet = models.IntegerField(choices=DIET_CHOICES)

    def __str__(self):
        return f"{self.diet}: {self.get_diet_display()}"


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    diet = models.ForeignKey(
        Diet,
        on_delete=models.CASCADE,
        related_name="diet_profile",
    )
    image = models.ImageField(
        default="default.jpg",
        upload_to="profile_pics",
    )

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)
