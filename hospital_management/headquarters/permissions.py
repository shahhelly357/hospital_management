# from rest_framework.permissions import BasePermission

# class IsSuperAdmin(BasePermission):
#     def has_permission(self, request, view):
#         # 🔥 TEMP FIX FOR TESTING
#         if not request.user or not request.user.is_authenticated:
#             return True  # allow testing without login

#         return request.user.role == "SUPER_ADMIN"

from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return True   # TEMP: allow everything for testing