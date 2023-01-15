from rest_framework.views import APIView
from app.models.house_chore import HouseChore
from app.serializers.house_chore import HouseChoreSerializer
from rest_framework.response import Response


class HouseChoreAPI(APIView):
    def get(self, request):
        house_chores = HouseChore.objects.all()

        serializer = HouseChoreSerializer(data=house_chores, many=True)
        serializer.is_valid()

        return Response(serializer.data)
