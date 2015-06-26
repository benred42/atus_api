from django.db import models


class Respondent(models.Model):
    stat_wt = models.FloatField()
    case_id = models.BigIntegerField(primary_key=True)
    youngest_child_age = models.IntegerField(default=0)
    age_edited = models.IntegerField(default=0)
    gender = models.IntegerField(default=0)
    education_level = models.IntegerField(default=0)
    race = models.IntegerField(default=0)
    is_hispanic = models.IntegerField(default=0)
    metropolitan_status = models.IntegerField(default=0)
    employment_status = models.IntegerField(default=0)
    has_multiple_jobs = models.IntegerField(default=0)
    work_status = models.IntegerField(default=0)
    is_student = models.IntegerField(default=0)
    school_level = models.IntegerField(default=0)
    partner_present = models.IntegerField(default=0)
    partner_employed = models.IntegerField(default=0)
    weekly_earnings_main = models.IntegerField(default=0)
    household_children = models.IntegerField(default=0)
    partner_work_status = models.IntegerField(default=0)
    weekly_hours_worked = models.IntegerField(default=0)
    date = models.IntegerField(default=0)
    is_holiday = models.IntegerField(default=0)
    eldercare_minutes = models.IntegerField(default=0)
    childcare_minutes = models.IntegerField(default=0)

def __str__(self):
        return str(self.case_id)


class Activity(models.Model):
    tier_1 = models.CharField(max_length=2)
    tier_2 = models.CharField(max_length=4)
    tier_3 = models.CharField(max_length=6)
    respondents = models.ManyToManyField(Respondent, through='Event')

    def __str__(self):
        return self.tier_3


class Event(models.Model):
    activity = models.ForeignKey(Activity)
    respondent = models.ForeignKey(Respondent)
    duration = models.FloatField()

    def __str__(self):
        return "{}: {}".format(self.respondent.case_id, self.activity.tier_3)
