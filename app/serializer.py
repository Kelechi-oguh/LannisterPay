from rest_framework import serializers
from .models import Transaction, SplitInfo, TransactionResponse, SplitBreakdown


class SplitInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplitInfo
        fields = ["SplitType", "SplitValue", "SplitEntityId"]


class TransactionSerializer(serializers.ModelSerializer):
    SplitInfo = SplitInfoSerializer(many=True)

    class Meta:
        model = Transaction
        fields = ["ID", "Amount", "Currency", "CustomerEmail", "SplitInfo"]

    def create(self, validated_data):
        split_info_data = validated_data.pop('SplitInfo')
        transaction = Transaction.objects.create(**validated_data)
        for data in split_info_data:
            SplitInfo.objects.create(transaction=transaction, **data)
        return transaction
    


class SplitBreakdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplitBreakdown
        fields = ["SplitEntityId", "Amount"]


class TransactionResponseSerializer(serializers.ModelSerializer):
    SplitBreakdown = SplitBreakdownSerializer(many=True)

    class Meta:
        model = TransactionResponse
        fields = ["ID", "Balance", "SplitBreakdown"]