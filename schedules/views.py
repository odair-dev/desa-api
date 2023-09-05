from .models import Schedule
from .serializers import ScheduleSerializer
from rest_framework.generics import ListCreateAPIView


class ScheduleView(ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    http_method_names = ["post", "get"]
