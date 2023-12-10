from django.urls import path

from API.AdminDashboard_DeskPage.views import UsersInformationList, UserChangeGoldAmount, UserChangeMoneyAmount

urlpatterns = [

    path('users-information-list/', UsersInformationList.as_view()),
    path('change-user-wallet-gold-amount/', UserChangeGoldAmount.as_view()),
    path('change-user-wallet-money-amount/', UserChangeMoneyAmount.as_view()),

]
