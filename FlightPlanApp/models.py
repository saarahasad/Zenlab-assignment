from django.db import models

class FlightPlan(models.Model):
    FlightPlanId = models.AutoField(primary_key=True, null=False)
    data = models.JSONField()



  
