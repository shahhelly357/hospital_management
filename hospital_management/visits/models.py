from django.db import models
from doctors.models import Doctor
from accounts.models import User


class Visit(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="visits")
    # mr = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visits")

    visit_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.doctor.name} - {self.status}"