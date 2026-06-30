from django.db import models


class HeadQuarter(models.Model):
    city = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.city


class SubHeadQuarter(models.Model):
    headquarter = models.ForeignKey(
        HeadQuarter,
        on_delete=models.CASCADE,
        related_name="areas"
    )
    area_name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.area_name} ({self.pincode})"