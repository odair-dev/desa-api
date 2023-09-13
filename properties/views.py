from .models import Property
from .serializers import PropertyInputSerializer, PropertyOutputSerializer, PropertyDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsSuperuserOrGet
from adresses.models import Address
from rest_framework import status
from rest_framework.response import Response


class PropertyView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrGet]

    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer
    http_method_names = ["post", "get"]

    def post(self, request, *args, **kwargs):
        serializer = PropertyInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        find_address = Address.objects.filter(
            **request.data['address']
        )

        if find_address:
            request.data['address'] = find_address[0].id
        else:
            new_address = Address.objects.create(
                **request.data['address']
            )
            request.data['address'] = new_address.id

        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = PropertyOutputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PropertyDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrGet]

    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer
    lookup_url_kwarg = "property_id"
    http_method_names = ["get", "patch", "delete"]

    def patch(self, request, *args, **kwargs):
        found_address = False
        for key in request.data:
            if key == 'address':
                found_address = True
        if found_address:
            find_address = Address.objects.filter(
                **request.data['address']
            )
            if find_address:
                request.data['address'] = find_address[0].id
            else:
                new_address = Address.objects.create(
                    **request.data['address']
                )
                request.data['address'] = new_address.id
        return self.partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = PropertyOutputSerializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)
