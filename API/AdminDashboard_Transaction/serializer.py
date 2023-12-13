from rest_framework import serializers

from Core.models.payment import PaymentTransactions


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:

        model = PaymentTransactions
        fields = '__all__'
