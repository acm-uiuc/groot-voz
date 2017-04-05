# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
This file is part of the Groot Project.
The Groot Project is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''

from flask import Flask, render_template
from flask_ask import Ask, statement, question
from utils import get_group, get_events
import os

app = Flask(__name__)
ask = Ask(app, '/')

PORT = 5652
DEBUG = os.environ.get('VOZ_DEBUG', False)


@ask.launch
def launch():
    welcome_text = render_template('welcome')
    help_text = render_template('help')
    return question(welcome_text).reprompt(help_text)


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


@ask.intent('UpcomingEventsIntent')
def upcoming_events():
    events = get_events()
    if not events:
        return statement(render_template('no_events'))
    response = render_template('events_intro')
    for event in events:
        response += render_template('events_single',
                                    name=event['name'],
                                    date=event['friendly_date'])
        response += '. '
    return statement(response)


@ask.intent('AMAZON.HelpIntent')
def help():
    help_text = render_template('help')
    return question(help_text)


@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Bye!")


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Bye!")


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
