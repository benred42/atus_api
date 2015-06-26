from api.models import Activity, Respondent, Event
from api.serializers import ActivitySerializer, RespondentSerializer, EventSerializer
from django.db.models import Sum, Count
from rest_framework import viewsets, generics


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all().annotate(
        weighted_average=(
            Sum('event__duration') / Sum('respondents__stat_wt'))).annotate(
        num_respondents=Count('respondents'))
    serializer_class = ActivitySerializer

#######################################################################################################################

class RespondentsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer

#######################################################################################################################

class EventView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer