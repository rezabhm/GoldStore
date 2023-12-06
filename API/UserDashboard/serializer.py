from rest_framework import serializers

from Core.models.gold import Wallet


class WalletDataSerializer(serializers.ModelSerializer):

    class Meta:

        model = Wallet
        fields = ['money_stock', 'gold_stock']
