from django.db import models
import datetime

class Weight(models.Model):
    date = models.DateField(default=datetime.date.today)
    weight = models.FloatField(default=150.0)
