from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .usermanager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    ROLE_CHOICES = (
        ('tenant', 'Tenant'),
        ('landlord', 'Landlord'),
    )
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
