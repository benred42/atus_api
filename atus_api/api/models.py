from django.db import models


class Respondent(models.Model):
    stat_wt = models.FloatField()
    case_id = models.IntegerField()

    def __str__(self):
        return self.case_id


class Activity(models.Model):
    tier_1 = models.CharField(max_length=2)
    tier_2 = models.CharField(max_length=4)
    tier_3 = models.CharField(max_length=6)

    def __str__(self):
        return self.tier_3


class Event(models.Model):
    activity = models.ForeignKey(Activity)
    respondent = models.ForeignKey(Respondent)
    duration = models.FloatField()
