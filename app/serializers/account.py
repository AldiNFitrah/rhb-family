from app.models.account import Account
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            "id",
            "holder_name",
            "number",
            "display_number",
            "balance",
            "type",
        )
