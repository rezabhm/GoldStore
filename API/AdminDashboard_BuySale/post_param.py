from rest_framework import serializers


class ProveSaleReqeustParam(serializers.Serializer):

    sale_request_id = serializers.FloatField()
