from rest_framework import serializers


class ProveMoneyGetRequestPostParam(serializers.Serializer):
    get_request_id = serializers.CharField()


class ProveGoldGetRequestPostParam(serializers.Serializer):
    get_request_id = serializers.CharField()


