from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from datetime import date

# Create your models here.

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
    
class Userprofiles(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    department = models.CharField(null=True)
    designation = models.CharField(null=True)
    created_at = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.name