from .models import Account
from .serializers import AccountSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperuserOrPost, IsSuperuserOrOwner


class AccountView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrPost]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    http_method_names = ["post", "get"]


class AccountDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuserOrOwner]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_url_kwarg = "account_id"
    http_method_names = ["get", "patch", "delete"]
