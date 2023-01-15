from rest_framework.views import APIView
from app.models.house_chore_reward_request import HouseChoreRewardRequest
from app.serializers.house_chore_reward_request import HouseChoreRewardRequestSerializer
from rest_framework.response import Response
from app.models.house_chore_reward_request import HouseChoreRewardRequest


class HouseChoreRewardRequestCreateAPI(APIView):
    def post(self, request):
        house_chore_reward_request = HouseChoreRewardRequest.objects.create(
            house_chore_id=request.data["house_chore_id"],
            requester_account_id=request.data["requester_account_id"],
            status=HouseChoreRewardRequest.Status.PENDING,
        )

        serializer = HouseChoreRewardRequestSerializer(house_chore_reward_request)

        return Response(serializer.data)


class HouseChoreRewardRequestListAPI(APIView):
    def get(self, request, user_id):
        pending_house_chore_reward_requests = HouseChoreRewardRequest.objects.filter(
            requester_account__parent_account__holder__id=user_id,
            status=HouseChoreRewardRequest.Status.PENDING,
        ).order_by('created_at')
        non_pending_house_chore_reward_requests = (
            HouseChoreRewardRequest.objects
                .filter(
                    requester_account__parent_account__holder__id=user_id
                )
                .exclude(
                    status=HouseChoreRewardRequest.Status.PENDING
                ).order_by('-created_at')
        )
        
        house_chore_reward_requests = [*pending_house_chore_reward_requests, *non_pending_house_chore_reward_requests]

        serializer = HouseChoreRewardRequestSerializer(data=house_chore_reward_requests, many=True)
        serializer.is_valid()

        return Response(serializer.data)
