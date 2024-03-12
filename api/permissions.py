from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.autor == request.user


class ReadOnlyOrIsAuthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        is_safe_method = (
            request.method in SAFE_METHODS)
        return is_authenticated or is_safe_method

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)
