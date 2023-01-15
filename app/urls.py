from django.urls import path  # noqa
from app.views.account import AccountAPI
from app.views.transfer_transaction import TransferTransactionCreateAPI
from app.views.house_chore import HouseChoreAPI
from app.views.house_chore_reward_request import (
    HouseChoreRewardRequestCreateAPI,
    HouseChoreRewardRequestListAPI,
)
from app.views.notification import NotificationAPI

app_urls = [
    path("users/<int:user_id>/accounts", AccountAPI.as_view()),
    path(
        "users/<int:user_id>/house-chores/reward-requests",
        HouseChoreRewardRequestListAPI.as_view(),
    ),
    path("transfer-transactions", TransferTransactionCreateAPI.as_view()),
    path("house-chores", HouseChoreAPI.as_view()),
    path("house-chores/reward-requests", HouseChoreRewardRequestCreateAPI.as_view()),
    path("notifications/<int:user_id>", NotificationAPI.as_view()),
]

urlpatterns = []
urlpatterns += app_urls
