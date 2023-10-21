from django.db import models

# Create your models here.

class userRank(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    deposit = models.IntegerField(default=1000000)
    earning_rate = models.FloatField(default=0)
