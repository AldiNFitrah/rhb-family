from django.db import models
from decimal import Decimal as D


class TransferTransaction(models.Model):
    origin_account_number = models.CharField(max_length=64)
    origin_account_holder_name = models.CharField(max_length=64)
    destination_account_number = models.CharField(max_length=64)
    destination_account_holder_name = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    fee = models.DecimalField(max_digits=20, decimal_places=2, default=D("0.0"))
    notes = models.TextField(null=True, blank=True)
