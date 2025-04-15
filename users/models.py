from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone_number = models.CharField(max_length=128, validators=[
      RegexValidator(
        regex=r'^\+?998?\d{9,13}$',
        message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
      ),
    ], blank=True, null=True)
    username = models.CharField(max_length=128, unique=True)
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)

    def __str__(self):
        return self.username
