from api.models import Activity
from rest_framework import serializers


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    code = serializers.PrimaryKeyRelatedField(source='tier_3', read_only=True)
    average_minutes = serializers.FloatField(read_only=True)
    total_respondents = serializers.IntegerField(read_only=True)

    class Meta:
        model = Activity
        fields = ('code', 'average_minutes', 'total_respondents')

