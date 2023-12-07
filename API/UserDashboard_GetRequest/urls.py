from django.urls import path

from API.UserDashboard_DeskPage.views import WalletData
from API.UserDashboard_GetRequest.views import GetRequestMoney, GetRequestGold

urlpatterns = [

    path('get-request-money/', GetRequestMoney.as_view()),
    path('get-request-gold/', GetRequestGold.as_view()),
    path('wallet-data/', WalletData.as_view()),

]
