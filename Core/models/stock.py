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
    request_status = models.CharField(max_length=20, choices=(

        ('تایید درخواست','تایید درخواست'),
        ('در انتظار بررسی', 'در انتظار بررسی'),
        ('رد درخواست', 'رد درخواست'),

    ), default='در انتظار بررسی')

    def __str__(self):
        return str(self.pk)


class BuyGold(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    buy_date = models.DateTimeField()
    money_amount = models.FloatField(default=0.0)
    gold_amount = models.FloatField(default=0.0)
    gold_price = models.ManyToManyField(GoldPrice)
    request_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


