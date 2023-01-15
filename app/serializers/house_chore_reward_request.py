from app.serializers.house_chore import HouseChoreSerializer
from app.serializers.account import AccountSerializer
from app.models.house_chore_reward_request import HouseChoreRewardRequest
from rest_framework import serializers


class HouseChoreRewardRequestSerializer(serializers.ModelSerializer):
    house_chore = HouseChoreSerializer()
    requester_account = AccountSerializer()

    class Meta:
        model = HouseChoreRewardRequest
        fields = ("id", "house_chore", "requester_account", "status", "created_at")
