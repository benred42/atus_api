from api.models import Activity
from api.serializers import ActivitySerializer
from rest_framework import generics


class ActivityListView(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer()
