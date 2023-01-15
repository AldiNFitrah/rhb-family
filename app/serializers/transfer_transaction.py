from app.models.transfer_transaction import TransferTransaction
from rest_framework import serializers


class TransferTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferTransaction
        fields = (
            "origin_account_number",
            "origin_account_holder_name",
            "destination_account_number",
            "destination_account_holder_name",
            "amount",
            "fee",
            "notes",
        )
