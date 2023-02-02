from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from FlightPlanApp.models import FlightPlan
from django.test import Client

class PostFlightPlanApiTestCase(APITestCase):
    def setUp(self):
        self.flightplan1 = FlightPlan.objects.create(
            FlightPlanId='15', data={
                "message": "FLIGHT PLAN APPROVAL REQUEST",
                "body": {
                    "flightPlan": {
                        "priority": "1",
                        "addressee": "CDMS",
                        "filing_time": "2023-01-26 18:11:20",
                        "originator": "PSU_DEMO_ID",
                        "message_type": "FPL",
                        "aircraft_identification": "DRONE_DEMO_ID_1",
                        "flight_rules": "I",
                        "type_of_flight": "D",
                        "number": "1",
                        "type_of_aircraft": "BA1",
                        "wake_turbulance_category": "L",
                        "equipment": "BE",
                        "departure_aerodrome": "IEE",
                        "time": "2023-01-26 18:13:20",
                        "route": [
                            "1",
                            "6",
                            "11",
                            "16",
                            "21",
                            "26",
                            "31"
                        ],
                        "destination_aerodrome": "IAF",
                        "total_eet": 104,
                        "1st alternate_aerodrome": "ECE",
                        "2nd_alternate_aerodrome": "CVH",
                        "supplementary_mandatory_information": {
                            "uav_address": "DRONE_DEMO_ID",
                            "src_vas_url": "http://localhost:5020",
                            "dst_vas_url": "http://localhost:5000"
                        },
                        "arrivalTime": "2023-01-26 18:16:00",
                        "cruiseSpeed": 15,
                        "Altitude": 130
                    }
                }
            })
        self.flightplan2 = FlightPlan.objects.create(
            FlightPlanId='16', data={
                "message": "FLIGHT PLAN APPROVAL REQUEST",
                "body": {
                    "flightPlan": {
                        "priority": "1",
                        "addressee": "CDMS",
                        "filing_time": "2023-01-26 18:11:20",
                        "originator": "PSU_DEMO_ID",
                        "message_type": "FPL",
                        "aircraft_identification": "DRONE_DEMO_ID_1",
                        "flight_rules": "I",
                        "type_of_flight": "D",
                        "number": "1",
                        "type_of_aircraft": "BA1",
                        "wake_turbulance_category": "L",
                        "equipment": "BE",
                        "departure_aerodrome": "IEE",
                        "time": "2023-01-26 18:13:20",
                        "route": [
                            "1",
                            "6",
                            "11",
                            "16",
                            "21",
                            "26",
                            "31"
                        ],
                        "destination_aerodrome": "IAF",
                        "total_eet": 104,
                        "1st alternate_aerodrome": "ECE",
                        "2nd_alternate_aerodrome": "CVH",
                        "supplementary_mandatory_information": {
                            "uav_address": "DRONE_DEMO_ID",
                            "src_vas_url": "http://localhost:5020",
                            "dst_vas_url": "http://localhost:5000"
                        },
                        "arrivalTime": "2023-01-26 18:16:00",
                        "cruiseSpeed": 15,
                        "Altitude": 130
                    }
                }
            })

    def test_create_flight_plan(self):
        input_flight_plan = {
            "data": {
                "message": "FLIGHT PLAN APPROVAL REQUEST",
                "body": {
                    "flightPlan": {
                        "priority": "1",
                        "addressee": "CDMS",
                        "filing_time": "2023-01-26 18:11:20",
                        "originator": "PSU_DEMO_ID",
                        "message_type": "FPL",
                        "aircraft_identification": "DRONE_DEMO_ID_1",
                        "flight_rules": "I",
                        "type_of_flight": "D",
                        "number": "1",
                        "type_of_aircraft": "BA1",
                                            "wake_turbulance_category": "L",
                                            "equipment": "BE",
                                            "departure_aerodrome": "IEE",
                                            "time": "2023-01-26 18:13:20",
                                            "route": [
                                                "1",
                                                "6",
                                                "11",
                                                "16",
                                                "21",
                                                "26",
                                                "31"
                                            ],
                        "destination_aerodrome": "IAF",
                        "total_eet": 104,
                        "1st alternate_aerodrome": "ECE",
                        "2nd_alternate_aerodrome": "CVH",
                        "supplementary_mandatory_information": {
                                                "uav_address": "DRONE_DEMO_ID",
                                                "src_vas_url": "http://localhost:5020",
                                                "dst_vas_url": "http://localhost:5000"
                                            },
                        "arrivalTime": "2023-01-26 18:16:00",
                        "cruiseSpeed": 15,
                        "Altitude": 130
                    }
                }
            }
        }
        response = self.client.post(
        reverse("flight_plan"), input_flight_plan, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_flight_plans(self):
        response = self.client.get(reverse("flight_plan"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_flight_plans(self):
        response = self.client.delete(reverse('flight_plan', kwargs={'pk': self.flightplan1.FlightPlanId}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_flight_plans(self):
        response = self.client.put(reverse('flight_plan', kwargs={'pk': self.flightplan2.FlightPlanId}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    