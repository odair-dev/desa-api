from .models import Schedule
from .serializers import ScheduleSerializer, ScheduleDetailSerializer, ScheduleInputSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .permissions import IsSuperuserOrOwner


class ScheduleCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleInputSerializer
    lookup_url_kwarg = "property_id"
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        request.data["account"] = request.user.id
        request.data["property"] = kwargs["property_id"]
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = ScheduleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ScheduleListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleDetailSerializer
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = Schedule.objects.filter(account=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ScheduleDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuserOrOwner]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleDetailSerializer
    lookup_url_kwarg = "schedule_id"
    http_method_names = ["get", "patch", "delete"]
