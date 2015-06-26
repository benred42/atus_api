import csv
import json
import datetime

"""
Models:
Activity:
    tier_1: 01
    tier_2: 0101
    tier_3: 010101

Event:
    id
    activity FK
    duration
    respondent FK

Respondent:
    stat_wt
    case_id PK
"""


rows = []
header = []
act_header = []

print("Converting activities...")
activities = []
with open("data/atussum_2014.dat") as infile:
    reader = csv.reader(infile)
    rows = [row for row in reader]

    header = rows[0]
    data = [row[24:] for row in rows[1:]]
    act_header = [row[24:] for row in rows[0:1]][0]  # Drop non-activities
    act_header = [code[1:] for code in act_header]  # Drop the leading t

    for activity_code in act_header:
        activities.append({"model": "api.Activity",
                           "pk": activity_code,
                           "fields": {
                                      "tier_1": activity_code[:2],
                                      "tier_2": activity_code[:4],
                                      "tier_3": activity_code
                                      }})

with open("atus_api/fixtures/activities.json", "w") as outfile:
    outfile.write(json.dumps(activities))


print("Converting respondents...")
demographic_data = [row[0:24] for row in rows[1:]]
demographic_titles =    ['case_id',
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
                         'childcare_minutes']
respondents = []

for row in demographic_data[:100]:
    fields_dict = {title: row[i] for (i,title) in enumerate(demographic_titles)}

    respondents.append({"model": "api.Respondent",
                        "pk": row[0],
                        "fields": fields_dict,
                        })

with open("atus_api/fixtures/respondents.json", "w") as outfile:
    outfile.write(json.dumps(respondents))


print("Converting events...")
events = []
event_pk_counter = 0
respondent_counter = 0

for row in rows[1:]:
    while event_pk_counter < 10000 or respondent_counter < 100:
        respondent_counter += 1
        case_id = row[0]
        tuflwigt = row[1]
        durations = row[24:]
        activities = act_header


        for i, duration in enumerate(durations):
            events.append({"model": "api.Event",
                            "pk": event_pk_counter,
                           "fields": {
                                      "respondent": case_id,
                                      "activity": activities[i],
                                      "duration": float(duration) * float(tuflwigt),
                                      }})
            event_pk_counter += 1

with open("atus_api/fixtures/events-subset.json", "w") as outfile:
    outfile.write(json.dumps(events))
