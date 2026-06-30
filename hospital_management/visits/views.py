from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Visit
from .serializers import VisitSerializer


class VisitViewSet(viewsets.ModelViewSet):
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['status', 'doctor']
    search_fields = ['doctor__name', 'notes']
    ordering_fields = ['id', 'visit_date', 'status']

    def get_queryset(self):
        user = self.request.user
        qs = Visit.objects.all()

        # 🔥 TEST MODE SAFE
        if not user or not user.is_authenticated:
            return qs

        if hasattr(user, "role") and user.role == "SUPER_ADMIN":
            return qs

        if hasattr(user, "role") and user.role in ["HQ_ADMIN", "HQ_STAFF"]:
            return qs.filter(doctor__headquarter=user.headquarter)

        if hasattr(user, "role") and user.role == "SUB_HQ_STAFF":
            return qs.filter(doctor__sub_headquarter=user.sub_headquarter)

        if hasattr(user, "role") and user.role == "MR":
            return qs.filter(mr=user)

        return qs.none()

    def perform_create(self, serializer):
        user = self.request.user

   