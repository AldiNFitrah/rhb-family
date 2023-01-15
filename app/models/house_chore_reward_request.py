from django.db import models
from app.models.house_chore import HouseChore
from app.models.account import Account


class HouseChoreRewardRequest(models.Model):
    class Status:
        PENDING = "pending"
        REJECTED = "rejected"
        APPROVED = "approved"

    STATUS_CHOICES = {
        Status.PENDING: "Pending",
        Status.REJECTED: "Rejected",
        Status.APPROVED: "Approved",
    }

    house_chore = models.ForeignKey(to=HouseChore, on_delete=models.RESTRICT)
    requester_account = models.ForeignKey(to=Account, on_delete=models.RESTRICT)
    status = models.CharField(
        max_length=32, choices=STATUS_CHOICES.items(), default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
