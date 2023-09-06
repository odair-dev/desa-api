from django_filters import rest_framework as filters
from .models import Address


class AddressFilter(filters.FilterSet):
    district = filters.CharFilter(
        field_name="district",
        lookup_expr="icontains"
    )
    city = filters.CharFilter(
        field_name="city",
        lookup_expr="icontains"
    )

    class Meta:
        model = Address
        fields = ["district", "city"]
