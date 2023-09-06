from .models import Category
from .serializers import CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsSuperuserOrGet


class CategoryView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrGet]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ["post", "get"]


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrGet]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = "category_id"
    http_method_names = ["get", "patch", "delete"]
