from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class PaymentTransactions(models.Model):

    payment_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    money_amount = models.FloatField(default=0.0)
    status = models.CharField(max_length=20,default=' در انتظار واریز وجه', choices=(

        (' در انتظار واریز وجه', ' در انتظار واریز وجه'),
        ('واریز موفقیت آمیز', 'واریز موفقیت آمیز'),
        ('واریز با حطا', 'واریز با حطا'),

    ))

    def __str__(self):
        return str(self.pk)
