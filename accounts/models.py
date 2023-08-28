from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator

class User(AbstractUser):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(
        unique=True, null=False, blank=False, validators=[EmailValidator]
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
