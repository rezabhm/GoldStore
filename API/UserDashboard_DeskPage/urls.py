from django.urls import path
from API.Home import views
from .views import *

urlpatterns = [

    path('gold-stock-price/', views.GoldStockPrice.as_view()),
    path('wallet-data/', WalletData.as_view()),

]
