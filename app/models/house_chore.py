from django.db import models


class HouseChore(models.Model):
    name = models.CharField(max_length=256)
    reward = models.DecimalField(max_digits=20, decimal_places=2)
    icon_url = models.URLField(null=True, blank=True)
