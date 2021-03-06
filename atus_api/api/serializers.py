from rest_framework.fields import SerializerMethodField
from api.models import Activity, Respondent, Event
from rest_framework import serializers
import api.code_list as atus
from rest_framework.reverse import reverse


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    code = serializers.PrimaryKeyRelatedField(read_only=True)
    average_minutes = serializers.FloatField(read_only=True,
                                             source='weighted_average')
    total_respondents = serializers.IntegerField(read_only=True,
                                                 source='num_respondents')
    titles = SerializerMethodField()
    filters = SerializerMethodField()

    def get_titles(self, obj):
        code = obj.code
        if len(obj.code) == 6:
            titles = [atus.code_dict[i] for i in
                      [code[0:2], code[0:4], code[0:6]]]
        elif len(obj.code) == 4:
            titles = [atus.code_dict[i] for i in [code[0:2], code[0:4]]]
        else:
            titles = [atus.code_dict[code]]
        return titles

    def get_filters(self, obj):
        filters = {key: value for key, value in
                   self.context.get('request').GET.items() if key != 'page'}
        return filters

    class Meta:
        model = Activity
        fields = (
            'url', 'code', 'average_minutes', 'total_respondents', 'titles',
            'filters')


#######################################################################################################################

class EventSerializer(serializers.HyperlinkedModelSerializer):
    activity_time = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ('activity_time',)

    def get_activity_time(self, obj):
        code = sorted([activity.code for activity in obj.activity.all()])[-1]
        return {code: (obj.duration / self.context.get('total_weight'))}


#######################################################################################################################

class RespondentSerializer(serializers.HyperlinkedModelSerializer):
    case_id = serializers.IntegerField(read_only=True)
    stat_wt = serializers.IntegerField(read_only=True)
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Respondent
        fields = ('case_id',
                  'url',
                  'stat_wt',
                  'youngest_child_age',
                  'age_edited',
                  'gender',
                  'education_level',
                  'race',
                  'is_hispanic',
                  'metropolitan_status',
                  'employment_status',
                  'has_multiple_jobs',
                  'work_status',
                  'is_student',
                  'school_level',
                  'partner_present',
                  'partner_employed',
                  'weekly_earnings_main',
                  'household_children',
                  'partner_work_status',
                  'weekly_hours_worked',
                  'date',
                  'is_holiday',
                  'eldercare_minutes',
                  'childcare_minutes',
                  '_links')

    def get__links(self, obj):
        links = {
            "activity_totals": reverse('event_list',
                                       kwargs=dict(respondent_id=obj.case_id),
                                       request=self.context.get('request')),
            "household_members": reverse('hhmembers_list',
                                         kwargs=dict(
                                             respondent_id=obj.case_id),
                                         request=self.context.get('request'))
        }
        return links


#######################################################################################################################

class HouseholdMemberSerializer(serializers.HyperlinkedModelSerializer):
    case_id = serializers.IntegerField(read_only=True)
    hhmember_id = serializers.IntegerField(read_only=True)
    age_edited = serializers.IntegerField(read_only=True)
    relationship = serializers.IntegerField(read_only=True)
    gender = serializers.IntegerField(read_only=True)
    age_flag = serializers.IntegerField(read_only=True)
    relationship_flag = serializers.IntegerField(read_only=True)
    gender_flag = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = (
        'case_id', 'hhmember_id', 'age_edited', 'relationship', 'gender',
        'age_flag', 'relationship_flag', 'gender_flag')

