from api.models import Activity, Respondent, Event
from api.serializers import ActivitySerializer, RespondentSerializer, EventSerializer
from django.db.models import Sum, Count
from rest_framework import viewsets, generics, filters
import django_filters


class ActivityFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(name="code", lookup_type="startswith")
    age__gt = django_filters.NumberFilter(name="event__respondent__age_edited", lookup_type="gt", distinct=True)
    age__lt = django_filters.NumberFilter(name="event__respondent__age_edited", lookup_type="lt", distinct=True)
    age = django_filters.RangeFilter(name="event__respondent__age_edited", distinct=True)
    work_status = django_filters.NumberFilter(name="event__respondent__work_status", lookup_type='exact', distinct=True)

    class Meta:
        model = Activity
        fields = ['code', 'age__gt', 'age__lt', 'age', 'work_status']

#######################################################################################################################


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    # total_weight = Respondent.objects.all().aggregate(Sum('stat_wt'))['stat_wt__sum']
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ActivityFilter

    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.

        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        for backend in list(self.filter_backends):
            total_weight = Respondent.objects.all().aggregate(Sum('stat_wt'))['stat_wt__sum']
            queryset = backend().filter_queryset(self.request, queryset, self)
            queryset = queryset.annotate(
                weighted_average=(
                    Sum('event__duration') / total_weight)).annotate(
                num_respondents=Count('event__respondent', distinct=True))
        return queryset


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
