from rest_framework.views import APIView
from app.models.account import Account
from app.serializers.account import AccountSerializer
from rest_framework.response import Response


class AccountAPI(APIView):
    def get(self, request, user_id):
        accounts = Account.objects.filter(holder_id=user_id)

        serializer = AccountSerializer(data=accounts, many=True)
        serializer.is_valid()

        return Response(serializer.data)
