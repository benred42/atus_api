from api.models import Activity, Respondent
from rest_framework import serializers


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    code = serializers.PrimaryKeyRelatedField(source='tier_3', read_only=True)
    average_minutes = serializers.FloatField(read_only=True, source='weighted_average')
    total_respondents = serializers.IntegerField(read_only=True, source='num_respondents')

    class Meta:
        model = Activity
        fields = ('code', 'average_minutes', 'total_respondents')

#######################################################################################################################

class RespondentSerializer(serializers.HyperlinkedModelSerializer):
    case_id = serializers.IntegerField(read_only=True)
    statistical_weight = serializers.IntegerField(source='stat_wt', read_only=True)

    class Meta:
        model = Respondent
        fields = ('case_id', 'statistical_weight')
