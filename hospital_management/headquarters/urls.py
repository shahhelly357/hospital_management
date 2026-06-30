from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeadQuarterViewSet, SubHeadQuarterViewSet

router = DefaultRouter()

router.register(r'hq', HeadQuarterViewSet, basename='hq')
router.register(r'sub-hq', SubHeadQuarterViewSet, basename='sub-hq')


urlpatterns = router.urls