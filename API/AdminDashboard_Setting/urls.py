from django.urls import path

from API.AdminDashboard_Setting.views import SettingData, ChangePrice, OpenCloseStock, ChangeStoreGoldAmount, \
    PriceDifference

urlpatterns = [

    path('setting-data/', SettingData.as_view()),
    path('change-gold-price/', ChangePrice.as_view()),
    path('open-close-stock/', OpenCloseStock.as_view()),
    path('change-warehouse-gold-amount/', ChangeStoreGoldAmount.as_view()),
    path('change-price-difference/', PriceDifference.as_view()),

]
