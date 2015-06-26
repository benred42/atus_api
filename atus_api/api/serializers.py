from api.models import Activity
from rest_framework import serializers


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    code = serializers.PrimaryKeyRelatedField(source=Activity.tier_3)
    average_minutes = serializers.FloatField(read_only=True)
    total_respondents = serializers.IntegerField(read_only=True)

    class Meta:
        model = Activity
        fields = ('code', 'average_minutes', 'total_respondents')

