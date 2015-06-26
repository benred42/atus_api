from api.models import Activity
from api.serializers import ActivitySerializer
from django.db.models import F, Sum
from rest_framework import viewsets


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all().annotate(
        weighted_average=(Sum(F('event__duration') * F('respondents__stat_wt')) / Sum('respondents__stat_wt')))
    serializer_class = ActivitySerializer
