from rest_framework import serializers


class Signup(serializers.Serializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    national_code = serializers.CharField()


class ProveCode(serializers.Serializer):

    phone_number = serializers.CharField()
    code = serializers.CharField()
