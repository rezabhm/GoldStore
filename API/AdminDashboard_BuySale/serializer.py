from rest_framework import serializers

from Core.models.stock import SaleGold, BuyGold


class SaleGoldSerializer(serializers.ModelSerializer):

    class Meta:

        model = SaleGold
        fields = '__all__'


class BuyGoldSerializer(serializers.ModelSerializer):

    class Meta:

        model = BuyGold
        fields = '__all__'
