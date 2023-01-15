from django.contrib import admin
from app.models import (
    Account,
    User,
    TransferTransaction,
    HouseChore,
    HouseChoreRewardRequest,
)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "holder_name", "display_number", "balance", "type")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "name", "phone_number")


@admin.register(TransferTransaction)
class TransferTransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "amount")


@admin.register(HouseChore)
class HouseChoreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "reward")

@admin.register(HouseChoreRewardRequest)
class HouseChoreAdmin(admin.ModelAdmin):
    list_display = ("id", "house_chore_id", "requester_account_id", "status")
