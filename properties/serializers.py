from rest_framework import serializers
from .models import Property
# from adresses.serializers import AddressSerializer


class PropertySerializer(serializers.ModelSerializer):
    # address = AddressSerializer()
    class Meta:
        model = Property
        fields = [
            "id",
            "enterprise",
            "sold",
            "address",
            "category",
        ]
        # extra_kwargs = {
        #     "category": {
        #         "read_only": True,
        #     }
        # }
        # categoria passada na URL
