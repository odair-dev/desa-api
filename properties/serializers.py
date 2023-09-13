from rest_framework import serializers
from .models import Property
from adresses.serializers import AddressSerializer
from categories.serializers import CategorySerializer


class PropertyInputSerializer(serializers.ModelSerializer):
    address = AddressSerializer(write_only=True)

    class Meta:
        model = Property
        fields = [
            "id",
            "enterprise",
            "sold",
            "address",
            "category"
        ]
        extra_kwargs = {
            "category": {
                "write_only": True,
            }
        }


class PropertyOutputSerializer(serializers.ModelSerializer):
    address_property = AddressSerializer(
        source="address",
        read_only=True,
    )
    category_property = CategorySerializer(
        source="category",
        read_only=True
    )

    class Meta:
        model = Property
        fields = [
            "id",
            "enterprise",
            "sold",
            "address",
            "category",
            "address_property",
            "category_property"
        ]
        extra_kwargs = {
            "address": {
                "write_only": True,
            },
            "category": {
                "write_only": True,
            }
        }


class PropertyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        depth = 2
        fields = [
            "id",
            "enterprise",
            "sold",
            "address",
            "category",
        ]
