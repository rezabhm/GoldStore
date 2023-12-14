from rest_framework import serializers

from Core.models.gold import GoldPrice


class GoldPriceSerializer(serializers.ModelSerializer):

    class Meta:

        model = GoldPrice
        fields = '__all__'
