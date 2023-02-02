from django.shortcuts import render
from FlightPlanApp.models import FlightPlan
from FlightPlanApp.serializers import FlightPlanSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

now = datetime.now() # current date and time

class FlightPlanApi(APIView):
    @csrf_exempt
    def post(self,request):
        serializer=FlightPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse({ "message": "CREATE FLIGHT PLAN" , "body":serializer.data })
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @csrf_exempt
    def get(self,request):
        flightplans = FlightPlan.objects.all()
        flightplan_serializer=FlightPlanSerializer(flightplans,many=True)
        return JsonResponse({ "flightplans": flightplan_serializer.data})
    @csrf_exempt
    def delete(self,request,pk,format=None):
        flightplan=FlightPlan.objects.get(FlightPlanId=pk)
        flightplan.delete()
        return JsonResponse({ "message": "DELETE FLIGHT PLAN" , "body":flightplan.data }) 
    @csrf_exempt
    def put(self,request,pk,format=None):
        flightplan=FlightPlan.objects.get(FlightPlanId=pk)
        flightdata = flightplan.data
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        flightdata['body']['flightPlan']['filing_time'] = date_time
        flightplan.data = flightdata
        flightplan.save()
        return JsonResponse({ "message": "UPDATE FLIGHT PLAN" , "body":flightplan.data }) 

