from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    # permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['headquarter', 'sub_headquarter', 'specialization']
    search_fields = ['name', 'specialization']
    ordering_fields = ['id', 'name']

    # def get_queryset(self):
    #     user = self.request.user
    #     qs = Doctor.objects.all()

    #     # SUPER ADMIN → full access
    #     if user.role == "SUPER_ADMIN":
    #         return qs

    #     # HQ ADMIN → only their HQ doctors
    #     if user.role == "HQ_ADMIN":
    #         return qs.filter(headquarter=user.headquarter)

    #     # HQ STAFF → same HQ doctors
    #     if user.role == "HQ_STAFF":
    #         return qs.filter(headquarter=user.headquarter)

    #     # SUB HQ STAFF → only their sub HQ doctors
    #     if user.role == "SUB_HQ_STAFF":
    #         return qs.filter(sub_headquarter=user.sub_headquarter)

    #     # MR → will later restrict via assignment table
    #     if user.role == "MR":
    #         return qs

    #     return qs.none()
    
    def get_queryset(self):
        user = self.request.user
        qs = Doctor.objects.all()

        # 🔥 TEST MODE SAFETY CHECK
        if not user or not hasattr(user, "role"):
            return qs   # allow everything in testing

        if user.role == "SUPER_ADMIN":
            return qs

        if user.role == "HQ_ADMIN":
            return qs.filter(headquarter=user.headquarter)

        if user.role == "HQ_STAFF":
            return qs.filter(headquarter=user.headquarter)

        if user.role == "SUB_HQ_STAFF":
            return qs.filter(sub_headquarter=user.sub_headquarter)

        if user.role == "MR":
            return qs   

        return qs.none()    