from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add any additional fields here if needed
    pass

    class Meta:
        # This prevents the conflicts with the default User model
        swappable = 'AUTH_USER_MODEL'