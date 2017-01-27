import requests
import arrow
from dateutil.parser import parse
from secrets import GROOT_URL, GROOT_ACCESS_TOKEN


def get_group(group):
    r = requests.get(GROOT_URL + '/groups/sigs',
                     headers=dict(Authorization=GROOT_ACCESS_TOKEN))
    try:
        return next(i for i in r.json() if i['name'].lower() == group.lower())
    except:
        raise ValueError('No group "%s"' % group)


def get_events():
    r = requests.get(GROOT_URL + '/events/upcoming',
                     headers=dict(Authorization=GROOT_ACCESS_TOKEN))
    events = r.json()
    for e in events:
        e['friendly_date'] = arrow.get(parse(e['start_time'])).humanize()
    return events
