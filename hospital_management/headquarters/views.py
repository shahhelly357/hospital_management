from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import HeadQuarter, SubHeadQuarter
from .serializers import HeadQuarterSerializer, SubHeadQuarterSerializer
from .permissions import IsSuperAdmin


class HeadQuarterViewSet(viewsets.ModelViewSet):
    queryset = HeadQuarter.objects.all()
    serializer_class = HeadQuarterSerializer

    permission_classes = [IsSuperAdmin]
    authentication_classes = []

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['city']
    search_fields = ['city']
    ordering_fields = ['id', 'city']
    
class SubHeadQuarterViewSet(viewsets.ModelViewSet):
    serializer_class = SubHeadQuarterSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['headquarter', 'area_name']
    search_fields = ['area_name']
    ordering_fields = ['id', 'area_name']

    # def get_queryset(self):
    #     user = self.request.user

    #     qs = SubHeadQuarter.objects.all()

    #     # SUPER ADMIN → full access
    #     if user.role == "SUPER_ADMIN":
    #         return qs

    #     # HQ ADMIN → only their HQ
    #     if user.role == "HQ_ADMIN":
    #         return qs.filter(headquarter=user.headquarter)

    #     # HQ STAFF → only their HQ
    #     if user.role == "HQ_STAFF":
    #         return qs.filter(headquarter=user.headquarter)

    #     # SUB HQ STAFF → only assigned sub HQ
    #     if user.role == "SUB_HQ_STAFF":
    #         return qs.filter(id=user.sub_headquarter_id)

    #     return SubHeadQuarter.objects.none()
    def get_queryset(self):
        user = self.request.user
        qs = SubHeadQuarter.objects.all()

        # 🔥 SAFE TEST MODE
        if not user or not hasattr(user, "role"):
            return qs

        if user.role == "SUPER_ADMIN":
            return qs

        if user.role == "HQ_ADMIN":
            return qs.filter(headquarter=user.headquarter)

        if user.role == "HQ_STAFF":
            return qs.filter(headquarter=user.headquarter)

        if user.role == "SUB_HQ_STAFF":
            return qs.filter(id=user.sub_headquarter_id)

        return qs.none()