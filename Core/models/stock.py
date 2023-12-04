from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .gold import GoldPrice


class SaleGold(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    sale_date = models.DateTimeField()
    money_amount = models.FloatField(default=0.0)
    gold_amount = models.FloatField(default=0.0)
    gold_price = models.ManyToManyField(GoldPrice)

    def __str__(self):
        return self.pk


class BuyGold(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    buy_date = models.DateTimeField()
    money_amount = models.FloatField(default=0.0)
    gold_amount = models.FloatField(default=0.0)
    gold_price = models.ManyToManyField(GoldPrice)
    buying_type = models.CharField(max_length=15, default='Add to Wallet', choices=(

                ('Add to Wallet', 'Add to Wallet'),
                ('get directly', 'get directly'),
            )
       )

    def __str__(self):
        return self.pk


