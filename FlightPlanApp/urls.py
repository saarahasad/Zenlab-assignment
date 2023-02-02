from django.conf.urls import url
from FlightPlanApp import views
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('fetch_flight_plans',views.FlightPlanApi.as_view(),name="flight_plan"),
    path('create_flight_plan',views.FlightPlanApi.as_view(),name="flight_plan"),
    path('delete_flight_plan/<int:pk>',views.FlightPlanApi.as_view(),name="flight_plan"),
    path('update_flight_plan/<int:pk>',views.FlightPlanApi.as_view(),name="flight_plan"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)