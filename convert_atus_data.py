import csv
import json

RESPONDENT_SUBSET_SIZE = 100
FIXTURE_DIR = 'atus_api/fixtures/'

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
                               "code": activity_code
                           }})

        activities.append({"model": "api.Activity",
                           "pk": activity_code[:4],
                           "fields": {
                               "code": activity_code[:4]
                           }})

        activities.append({"model": "api.Activity",
                           "pk": activity_code[:2],
                           "fields": {
                               "code": activity_code[:2]
                           }})

with open(FIXTURE_DIR + "activities.json", "w") as outfile:
    outfile.write(json.dumps(activities))

print("Converting respondents...")
demographic_data = [row[0:24] for row in rows[1:]]
demographic_titles = ['case_id',
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

for row in demographic_data[:RESPONDENT_SUBSET_SIZE]:
    fields_dict = {title: row[i] for (i, title) in enumerate(demographic_titles)}

    respondents.append({"model": "api.Respondent",
                        "pk": row[0],
                        "fields": fields_dict,
                        })

with open(FIXTURE_DIR + "respondents.json", "w") as outfile:
    outfile.write(json.dumps(respondents))

print("Converting events...")
events = []
event_pk_counter = 0
respondent_counter = 0

split_length = 3000
split_num = 1

for row in rows[1:]:
    if respondent_counter < RESPONDENT_SUBSET_SIZE:
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
                               "activity": [activities[i][:2], activities[i][:4], activities[i]],
                               "duration": float(duration) * float(tuflwigt),
                           }})
            event_pk_counter += 1
            # if event_pk_counter % split_length == 0:
            #     split_count = event_pk_counter // split_length
            #     filename = FIXTURE_DIR + "events-" + str(split_count) + ".json"
            #     with open(filename, "w") as outfile:
            #         outfile.write(json.dumps(events))
            #     events = []


with open(FIXTURE_DIR + "events-final.json", "w") as outfile:
    outfile.write(json.dumps(events))


print("Converting hhmembers...")
with open("data/atusrost_2014.dat") as infile:
    reader = csv.reader(infile)
    rows = [row for row in reader]
    header = rows[0]

    hhmembers = []
    unique_case_ids = 0
    hhmember_pk_counter = 0

    for row in rows[1:]:
        if int(row[1]) == 1:
            unique_case_ids += 1
        if unique_case_ids <= RESPONDENT_SUBSET_SIZE:
            hhmembers.append({"model": "api.HouseholdMember",
                              "pk": hhmember_pk_counter,
                              "fields": {
                                  "respondent": row[0],
                                  "hhmember_id": row[1],
                                  "age_edited": row[2],
                                  "relationship": row[3],
                                  "gender": row[4],
                                  "age_flag": row[5],
                                  "relationship_flag": row[6],
                                  "gender_flag": row[7],
                              }})
            hhmember_pk_counter += 1

with open(FIXTURE_DIR + "hhmembers.json", "w") as outfile:
    outfile.write(json.dumps(hhmembers))
