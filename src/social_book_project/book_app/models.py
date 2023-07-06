from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from datetime import date

# Create your models here.

class Book(models.Model):
    email = models.EmailField(_("Email ID"), unique=True)
    phone = models.PositiveBigIntegerField(_("Phone no."), unique=True)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    Public_visibility = models.BooleanField(_("Public Visibility"), default=False)
    phone = models.BigIntegerField(_("Phone no."), unique=True)
    birth_year = models.DateField(_("Year of Birth"), unique=False)
    password = models.CharField(_("Password"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone', 'birth_year']

    objects = CustomUserManager()

    def __str__(self):
        return self.email