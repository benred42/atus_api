from rest_framework.fields import SerializerMethodField
from api.models import Activity, Respondent, Event
from rest_framework import serializers
import api.code_list as atus
from rest_framework.reverse import reverse


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    code = serializers.PrimaryKeyRelatedField(source='tier_3', read_only=True)
    average_minutes = serializers.FloatField(read_only=True, source='weighted_average')
    total_respondents = serializers.IntegerField(read_only=True, source='num_respondents')
    titles = SerializerMethodField()

    def get_titles(self, obj):
        code = obj.tier_3
        titles = [atus.code_dict[i] for i in [code[0:2], code[0:4], code[0:6]]]
        return titles

    class Meta:
        model = Activity
        fields = ('url', 'code', 'average_minutes', 'total_respondents', 'titles')


#######################################################################################################################

class EventSerializer(serializers.HyperlinkedModelSerializer):
    activity_time = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ('activity_time',)

    def get_activity_time(self, obj):
        return {obj.activity.tier_3: (obj.duration/self.context.get('total_weight'))}


#######################################################################################################################

class RespondentSerializer(serializers.HyperlinkedModelSerializer):
    case_id = serializers.IntegerField(read_only=True)
    statistical_weight = serializers.IntegerField(source='stat_wt', read_only=True)
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Respondent
        fields = ('url', 'case_id', 'statistical_weight', '_links')

    def get__links(self, obj):
        links = {
            "activity_totals": reverse('event_list', kwargs=dict(respondent_id=obj.case_id),
                                       request=self.context.get('request'))}
        return links
