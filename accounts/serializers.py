from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)

    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = [
            "id",
            "name",
            "phone",
            "email",
            "username",
            "password",
            "is_superuser"
        ]
