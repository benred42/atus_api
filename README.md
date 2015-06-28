# ATUS API

## Normal Mode

Download the data files for the 2014 [American Time Use Survey](http://www.bls.gov/tus/home.htm).
Using PostgreSQL and Django, model this data and insert it into your database.

You will then build a read-only JSON API with Django REST Framework to allow
people to search and analyze this data. All list views should allow pagination
and filtering on appropriate fields.

**NOTE: All sample URLs and responses below are just that: samples. You should
design your API as you see fit, not to replicate them.**

First, make endpoints for looking at all and individual respondents.
Respondents should have, in addition to their demographic data, their
statistical weight and the minute count for each of their activities. The
minute counts should be nested in a dictionary with a key like
"activity_totals".

Example (with many fields not shown):

```json
{"case_id": "20060101020210",
 "statistical_weight": 22261358.19,
 "labor_force_status": 1,
 "age": 26,
 ...
 "activity_totals": {
   "010101": 480,
   "010102": 0,
   "180501": 30,
   ...
 }
}
```

Respondents have these nested endpoints:

* Household members.
* Activities. This should show all activities recorded by that respondent.

Next, make endpoints for looking at each activity code. You can specify
a two-digit, four-digit, or six-digit code and get summarized data for that
activity or set of activities.

A sample result might look like:

```json
{"code": "010101",
 "titles": ["Personal Care", "Sleeping", "Sleeping"],
 "average_minutes": 415.0,
 "total_respondents": 20000,
 "filter": {}}
```

Use [django-filter](https://django-filter.readthedocs.org/en/latest/) and
[filtering in Django REST Framework](https://django-filter.readthedocs.org/en/latest/)
to allow for filtering this down from all respondents to a subset. django-filter
allows for many lookup types. If I wanted to see how many minutes employed
people between the ages of 30 and 40 slept on average, I could craft a URL like
`/activities/0101/?age__gte=30&age__lt=40&labor_force_status=1` and get a result
like:

```json
{
  "code": "0101",
  "titles": ["Personal Care", "Sleeping"],
  "average_minutes": 428.5,
  "total_respondents": 1580,
  "filter": {
     "age__gte": 30,
     "age__lt": 40,
     "labor_force_status": 1
  }
}
```

## Hard Mode

Add endpoints for all the fields respondents have, showing their description
as well as the valid values for them. An example with the sample URL `/fields/labor_force_status`:

```json
{
  "name": "labor_force_status",
  "description": "The current working status of the respondent.",
  "original_name": "TELFS",
  "values": {
    "1": "Employed - at work",
    "2": "Employed - absent",
    "3": "Unemployed - on layoff",
    "4": "Unemployed - looking",
    "5": "Not in labor force"
  }
}
```

## Nightmare Mode

Add an option to get XML or CSV instead of JSON from your API.
