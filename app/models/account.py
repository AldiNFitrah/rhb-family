from django.db import models
from app.models.user import User


class Account(models.Model):
    parent_account = models.ForeignKey(
        to='self',
        on_delete=models.RESTRICT,
        related_name="child_accounts",
        null=True,
        blank=True,
    )
    holder = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="accounts"
    )
    number = models.CharField(max_length=64, unique=True)
    display_number = models.CharField(max_length=64, null=True, blank=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.CharField(max_length=64)

    @property
    def holder_name(self):
        return self.holder.name

    def save(self, *args, **kwargs):
        self.display_number = self.number

        self.number = ''.join(c for c in self.number if c.isdigit())

        return super().save(*args, **kwargs)
