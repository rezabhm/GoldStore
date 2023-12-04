from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Wallet(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money_stock = models.FloatField(default=0.0)
    gold_stock = models.FloatField(default=0.0)

    def __str__(self):
        return self.user


class GoldPrice(models.Model):

    Date = models.DateTimeField()
    sale_price = models.FloatField(default=2500000)
    price_difference = models.FloatField(default=10000)
    total_gold_stock = models.FloatField(default=0.0)
    stock_status = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.pk)
