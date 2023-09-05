from rest_framework import permissions
from rest_framework.views import View, Request


class IsSuperuserOrPost(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (request.user.is_authenticated and request.user.is_superuser or request.method == "POST")


class IsSuperuserOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user.is_superuser or request.user == obj)
