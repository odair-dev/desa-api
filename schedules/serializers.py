from rest_framework import serializers
from .models import Schedule
from adresses.serializers import AddressSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            "id",
            "date",
            "hour",
            "property",
            "account",
        ]


class ScheduleInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            "id",
            "date",
            "hour",
        ]


class ScheduleDetailSerializer(serializers.ModelSerializer):
    property = serializers.CharField(
        source="property.enterprise",
        read_only=True
    )
    address = AddressSerializer(
        source="property.address",
        read_only=True,
    )
    account = serializers.CharField(
        source="account.name",
        read_only=True
    )

    class Meta:
        model = Schedule
        fields = [
            "id",
            "date",
            "hour",
            "account",
            "property",
            "address",
        ]
