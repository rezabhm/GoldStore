from django.db import models
from django.contrib.auth.models import User


class UserInformation(models.Model):

    user_type = models.CharField(max_length=10, default='customer', choices=(

                ('admin', 'admin'),
                ('customer', 'customer'),

            )
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    joined_date = models.DateTimeField(null=True)
    national_code = models.CharField(max_length=13)

    auth_temp_code = models.CharField(null=True, max_length=8)
    auth_temp_code_create_date = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.user.username)


class SmsMSG(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(default='')
    sendDate = models.DateTimeField()

    def __str__(self):
        return self.message
