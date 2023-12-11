from django.urls import path

from API.AdminDashboard_GetRequest.views import MoneyGetRequestList, ProveMoneyGetRequest

urlpatterns = [

    path('money-get-request-list/', MoneyGetRequestList.as_view()),
    path('prove-money-get-request/', ProveMoneyGetRequest.as_view()),

]
