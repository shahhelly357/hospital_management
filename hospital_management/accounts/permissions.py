from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "SUPER_ADMIN"
        )


class IsHQAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "HQ_ADMIN"
        )


class IsHQStaff(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "HQ_STAFF"
        )


class IsSubHQStaff(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "SUB_HQ_STAFF"
        )


class IsMR(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "MR"
        )


class IsHQOrAbove(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role in ["SUPER_ADMIN", "HQ_ADMIN"]
        )


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role in [
                "HQ_ADMIN",
                "HQ_STAFF",
                "SUB_HQ_STAFF"
            ]
        )