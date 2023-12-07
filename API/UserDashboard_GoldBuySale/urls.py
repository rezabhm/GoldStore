from django.urls import path

from API.UserDashboard_GoldBuySale.views import SaleGoldRequest, BuyGoldRequest

urlpatterns = [

    path('sale-gold/', SaleGoldRequest.as_view()),
    path('buy-gold/', BuyGoldRequest.as_view()),

]
