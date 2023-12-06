from django.db import models
from django.contrib.auth.models import User


class MoneyGetRequest(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    request_date = models.DateTimeField()
    money_amount = models.FloatField(default=0.0)
    request_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


class GoldGetRequest(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    request_date = models.DateTimeField()
    gold_amount = models.FloatField(default=0.0)
    request_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)
