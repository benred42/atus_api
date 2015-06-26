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




print("Converting activities...")
users = []
with open("data/atussum_2014.dat") as infile:
    reader = csv.reader(infile)
    rows = [row for row in reader]

    header = rows[0]
    data = [row[24:] for row in rows[1:]]
    act_header = [row[24:] for row in rows[0:1]][0]  # Drop non-activities
    act_header = [code[1:] for code in act_header]  # Drop the leading t

    for activity_code in act_header:
        users.append({"model": "api.Activity",
                      "pk": activity_code,
                      "fields": {
                          "tier_1": activity_code[:2],
                          "tier_2": activity_code[:4],
                          "tier_3": activity_code
                      }})

with open("atus_api/fixtures/activities.json", "w") as outfile:
    outfile.write(json.dumps(users))
