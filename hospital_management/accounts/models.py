from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = [
        ("SUPER_ADMIN", "Super Admin"),
        ("HQ_ADMIN", "HQ Admin"),
        ("HQ_STAFF", "HQ Staff"),
        ("SUB_HQ_STAFF", "Sub HQ Staff"),
        ("MR", "Medical Representative"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="MR"
    )

    def __str__(self):
        return f"{self.username} ({self.role})"