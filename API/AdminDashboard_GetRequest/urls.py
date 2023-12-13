from django.urls import path

from API.AdminDashboard_GetRequest.views import MoneyGetRequestList, ProveMoneyGetRequest, GoldGetRequestList, \
    ProveGoldGetRequest

urlpatterns = [

    path('money-get-request-list/', MoneyGetRequestList.as_view()),
    path('prove-money-get-request/', ProveMoneyGetRequest.as_view()),

    path('gold-get-request-list/', GoldGetRequestList.as_view()),
    path('prove-gold-get-request/', ProveGoldGetRequest.as_view()),

]
