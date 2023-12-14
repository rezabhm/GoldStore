from django.urls import path

from API.AdminDashboard_BuySale.views import SaleList, BuyList, ProveSaleRequest

urlpatterns = [

    path('sale-list/', SaleList.as_view()),
    path('buy-list/', BuyList.as_view()),
    path('prove-sale-request/', ProveSaleRequest.as_view()),

]
