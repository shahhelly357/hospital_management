from django.db import models
from django.core.validators import RegexValidator
from headquarters.models import HeadQuarter, SubHeadQuarter

phone_validator = RegexValidator(
    regex=r'^[0-9]{10}$',
    message="Phone number must be exactly 10 digits."
)


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    phone = models.CharField(
        max_length=10,
        validators=[phone_validator]
    )

    headquarter = models.ForeignKey(
        HeadQuarter,
        on_delete=models.CASCADE,
        related_name="doctors"
    )

    sub_headquarter = models.ForeignKey(
        SubHeadQuarter,
        on_delete=models.CASCADE,
        related_name="doctors"
    )

    def __str__(self):
        return self.name