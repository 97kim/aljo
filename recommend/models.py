from django.db import models
from django.conf import settings

class Recommend(models.Model):
    q1 = models.IntegerField(null=True)
    q2 = models.IntegerField(null=True)
    q3 = models.IntegerField(null=True)
    q4 = models.IntegerField(null=True)
    q5 = models.IntegerField(null=True)
    q6 = models.IntegerField(null=True)
    q7 = models.IntegerField(null=True)
    q8 = models.IntegerField(null=True)
    q9 = models.IntegerField(null=True)
    q10 = models.IntegerField(null=True)
    q11 = models.IntegerField(null=True)
    q12 = models.IntegerField(null=True)
    q13 = models.IntegerField(null=True)
    q14 = models.IntegerField(null=True)
    q15 = models.IntegerField(null=True)
    q16 = models.IntegerField(null=True)
    q17 = models.IntegerField(null=True)
    q18 = models.IntegerField(null=True)
    q19 = models.IntegerField(null=True)
    q20 = models.IntegerField(null=True)

    def __str__(self):
        return self.user
