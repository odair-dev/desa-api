from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    account_id = serializers.CharField(
        source="account.id",
        read_only=True
    )
    account_name = serializers.CharField(
        source="account.name",
        read_only=True
    )
    account_phone = serializers.CharField(
        source="account.phone",
        read_only=True
    )
    account = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = Schedule
        fields = [
            "id",
            "date",
            "hour",
            "property",
            "account",
            "account_id",
            "account_name",
            "account_phone",
        ]
