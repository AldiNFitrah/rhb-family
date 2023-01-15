from app.models.house_chore import HouseChore
from rest_framework import serializers


class HouseChoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseChore
        fields = (
            "id",
            "name",
            "reward",
            "icon_url",
        )
