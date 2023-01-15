from rest_framework.views import APIView
from app.models.transfer_transaction import TransferTransaction
from app.models.account import Account
from app.models.house_chore_reward_request import HouseChoreRewardRequest
from app.serializers.transfer_transaction import TransferTransactionSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import transaction
from decimal import Decimal as D
from django.core.exceptions import BadRequest


class TransferTransactionCreateAPI(APIView):
    @transaction.atomic
    def post(self, request):
        transfer_transaction = TransferTransaction.objects.create(
            origin_account_number=request.data["origin_account_number"],
            origin_account_holder_name=request.data["origin_account_holder_name"],
            destination_account_number=request.data["destination_account_number"],
            destination_account_holder_name=request.data[
                "destination_account_holder_name"
            ],
            amount=D(request.data["amount"]),
            notes=request.data.get("notes"),
        )

        origin_account = Account.objects.get(
            number=transfer_transaction.origin_account_number
        )
        origin_account.balance -= transfer_transaction.amount
        origin_account.save()

        destination_account = Account.objects.filter(
            number=transfer_transaction.destination_account_number
        ).first()
        if destination_account is not None:
            destination_account.balance += transfer_transaction.amount
            destination_account.save()

        house_chore_reward_request_id = request.data.get(
            "house_chore_reward_request_id"
        )
        if house_chore_reward_request_id is not None:
            house_chore_reward_request = get_object_or_404(
                klass=HouseChoreRewardRequest, id=house_chore_reward_request_id
            )

            if (
                house_chore_reward_request.status
                != HouseChoreRewardRequest.Status.PENDING
            ):
                raise BadRequest("This request has been processed before")

            house_chore_reward_request.status = HouseChoreRewardRequest.Status.APPROVED
            house_chore_reward_request.save()

        serializer = TransferTransactionSerializer(transfer_transaction)

        return Response(serializer.data)
