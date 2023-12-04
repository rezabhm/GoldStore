from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserInformation(models.Model):

    user_type = models.CharField(max_length=10, default='customer', choices=(

                ('admin', 'admin'),
                ('customer', 'customer'),

            )
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    joined_date = models.DateTimeField()
    national_code = models.CharField(max_length=13)

    def __str__(self):
        return self.user


class SmsMSG(models.Model):

    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    message = models.TextField(default='')
    sendDate = models.DateTimeField()

    def __str__(self):
        return self.message
