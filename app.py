from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')


@ask.intent('GroupMeetingIntent',
    mapping={'group': 'Group'})
def meeting(group):
    speech_text = "Hello %s" % group
    return statement(speech_text)


def _supported_groups():
    pass

if __name__ == '__main__':
    app.run()
