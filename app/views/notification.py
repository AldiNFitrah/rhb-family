from rest_framework.views import APIView
from app.models.house_chore_reward_request import HouseChoreRewardRequest
from app.serializers.account import AccountSerializer
from rest_framework.response import Response


class NotificationAPI(APIView):
    def get(self, request, user_id):
        house_chore_reward_requests = HouseChoreRewardRequest.objects.filter(
            requester_account__parent_account__holder__id=user_id,
            status=HouseChoreRewardRequest.Status.PENDING,
        )

        is_exists_new_notification = house_chore_reward_requests.exists()

        return Response({"is_exists_new_notification": is_exists_new_notification})
