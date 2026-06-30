# from rest_framework.permissions import BasePermission


# class VisitPermission(BasePermission):

#     def has_permission(self, request, view):
#         user = request.user

#         # allow only logged-in users later
#         return True

#     def has_object_permission(self, request, view, obj):
#         user = request.user

#         if not user or not hasattr(user, "role"):
#             return True

#         if user.role == "SUPER_ADMIN":
#             return True

#         if user.role == "HQ_ADMIN":
#             return obj.headquarter == user.headquarter

#         if user.role == "HQ_STAFF":
#             return obj.headquarter == user.headquarter

#         if user.role == "SUB_HQ_STAFF":
#             return obj.sub_headquarter == user.sub_headquarter

#         if user.role == "MR":
#             return obj.assigned_to == user 

#         return False

from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return True   # TEMP: allow everything for testing