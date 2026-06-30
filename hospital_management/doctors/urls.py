from django.urls import path, include
from rest_framework.routers import DefaultRouter

from doctors.views import DoctorViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')

urlpatterns = router.urls