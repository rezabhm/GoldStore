from django.contrib import admin

from .models import user
from .models import gold
from .models import payment
from .models import stock
from .models import request

# Register your models here.
admin.register(user.UserInformation)
admin.register(user.SmsMSG)

admin.register(gold.GoldPrice)
admin.register(gold.Wallet)

admin.register(payment.PaymentTransactions)

admin.register(request.MoneyGetRequest)
admin.register(request.GoldGetRequest)

admin.register(stock.BuyGold)
admin.register(stock.SaleGold)
