from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class PaymentTransactions(models.Model):

    payment_date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    money_amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.pk
