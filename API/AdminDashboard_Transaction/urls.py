from django.urls import path

from API.AdminDashboard_Transaction.views import TransactionList

urlpatterns = [

    path('transaction-list/', TransactionList.as_view()),

]