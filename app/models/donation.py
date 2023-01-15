from django.db import models


class Donation(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
