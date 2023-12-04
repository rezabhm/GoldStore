from django.urls import re_path
from .views import *

urlpatterns = [

    re_path('gold-stock-price/', GoldStockPrice.as_view()),
    re_path('validate-token/', ValidateToken.as_view()),

]
