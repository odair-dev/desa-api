from .models import Property
from .serializers import PropertySerializer
from rest_framework.generics import ListCreateAPIView


class PropertyView(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    http_method_names = ["post", "get"]
