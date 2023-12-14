from django.contrib.auth.models import User
from rest_framework import serializers


class UsersInformationListSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['id', 'first_name', 'last_name', 'username']
