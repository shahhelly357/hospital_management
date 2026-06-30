from rest_framework import serializers
from .models import HeadQuarter, SubHeadQuarter
class HeadQuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadQuarter
        fields = "__all__"
        
class SubHeadQuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubHeadQuarter
        fields = "__all__"