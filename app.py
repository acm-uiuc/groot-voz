from flask import Flask, render_template
from flask_ask import Ask, statement
import requests
from secrets import GROOT_URL, GROOT_ACCESS_TOKEN

app = Flask(__name__)
ask = Ask(app, '/')


@ask.intent('GroupMeetingIntent',
            mapping={'group': 'Group'})
def meeting_time(group):
    group = group.lower().replace(' ', '')
    try:
        group_info = get_group(group)
    except:
        return statement(render_template('group_unknown'))

    response = render_template('group_meeting_time_response',
                               group=group, day=group_info['meetingDay'],
                               time=group_info['meetingTime'])
    return statement(response)


def get_group(group):
    r = requests.get(GROOT_URL + '/groups/sigs',
                     headers=dict(Authorization=GROOT_ACCESS_TOKEN))
    try:
        return next(i for i in r.json() if i['name'].lower() == group.lower())
    except:
        raise ValueError('No group "%s"' % group)


if __name__ == '__main__':
    app.run(debug=True)
