from .models import Address
from .serializers import AddressSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsSuperuserOrGet
from .filters import AddressFilter


class AddressView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrGet]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    http_method_names = ["post", "get"]
    filterset_class = AddressFilter


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrGet]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_url_kwarg = "address_id"
    http_method_names = ["get", "patch", "delete"]
