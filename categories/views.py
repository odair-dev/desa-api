from .models import Category
from .serializers import CategorySerializer
from rest_framework.generics import ListCreateAPIView


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ["post", "get"]
