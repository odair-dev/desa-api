from .models import Address
from .serializers import AddressSerializer
from rest_framework.generics import ListCreateAPIView


class AddressView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    http_method_names = ["post", "get"]
