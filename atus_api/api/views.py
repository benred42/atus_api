from api.models import Activity
from api.serializers import ActivitySerializer
from rest_framework import viewsets


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
