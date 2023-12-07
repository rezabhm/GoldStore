from django.urls import path

from API.UserDashboard_UserReporting.views import BuyGoldReport, SaleGoldReport, GetGoldRequestReport, \
    GetMoneyRequestReport, TransactionReport

urlpatterns = [

    path('buy-gold-report/', BuyGoldReport.as_view()),
    path('sale-gold-report/', SaleGoldReport.as_view()),
    path('get-gold-request-report/', GetGoldRequestReport.as_view()),
    path('get-money-request-report/', GetMoneyRequestReport.as_view()),
    path('transaction-report/', TransactionReport.as_view()),

]