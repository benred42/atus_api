from api.models import Activity, Respondent, Event
from api.serializers import ActivitySerializer, RespondentSerializer, EventSerializer
from django.db.models import Sum, Count
from rest_framework import viewsets, generics, filters
import django_filters


class ActivityFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(name="code", lookup_type="startswith")

    class Meta:
        model = Activity
        fields = ['code']

#######################################################################################################################


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    total_weight = Respondent.objects.all().aggregate(Sum('stat_wt'))['stat_wt__sum']
    queryset = Activity.objects.all().annotate(
        weighted_average=(
            Sum('event__duration') / total_weight)).annotate(
        num_respondents=Count('event__respondent', distinct=True))
    serializer_class = ActivitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ActivityFilter

#######################################################################################################################

class RespondentsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer

#######################################################################################################################

class EventView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        self.total_weight = Respondent.objects.all().aggregate(Sum('stat_wt'))['stat_wt__sum']
        queryset = Event.objects.all().filter(respondent__case_id=self.kwargs['respondent_id'])
        return queryset

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'total_weight': self.total_weight
        }
