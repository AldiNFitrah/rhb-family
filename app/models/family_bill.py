from django.db import models


class FamilyBill(models.Model):
    deadline = models.DateTimeField()
    total_bill = models.DecimalField(max_digits=20, decimal_places=2)
    current_total = models.DecimalField(max_digits=20, decimal_places=2)
    name = models.CharField(max_length=256)
