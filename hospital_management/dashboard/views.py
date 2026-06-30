from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

from headquarters.models import HeadQuarter, SubHeadQuarter
from doctors.models import Doctor
from visits.models import Visit


class DashboardAPIView(APIView):

    def get(self, request):

        today = timezone.now().date()

        data = {
            "total_hq": HeadQuarter.objects.count(),
            "total_sub_hq": SubHeadQuarter.objects.count(),
            "total_doctors": Doctor.objects.count(),
            

            "todays_visits": Visit.objects.filter(visit_date=today).count(),
            "completed_visits": Visit.objects.filter(status="COMPLETED").count(),
            "pending_visits": Visit.objects.filter(status="PENDING").count(),
        }

        return Response(data)