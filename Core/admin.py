from django.contrib import admin

from .models import user
from .models import gold
from .models import payment
from .models import stock
from .models import request

# Register your models here.
admin.site.register(user.UserInformation)
admin.site.register(user.SmsMSG)

admin.site.register(gold.GoldPrice)
admin.site.register(gold.Wallet)

admin.site.register(payment.PaymentTransactions)

admin.site.register(request.MoneyGetRequest)
admin.site.register(request.GoldGetRequest)

admin.site.register(stock.BuyGold)
admin.site.register(stock.SaleGold)
