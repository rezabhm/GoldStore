from django.urls import path

from API.UserDashboard_DeskPage.views import WalletData
from API.UserDashboard_GoldBuySale.views import SaleGoldRequest, BuyGoldRequest

urlpatterns = [

    path('sale-gold/', SaleGoldRequest.as_view()),
    path('buy-gold/', BuyGoldRequest.as_view()),
    path('wallet-data/', WalletData.as_view()),

]
