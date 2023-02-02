from rest_framework import serializers
from FlightPlanApp.models import FlightPlan

class FlightPlanSerializer(serializers.ModelSerializer):
     class Meta:
        model=FlightPlan 
        fields='__all__'


