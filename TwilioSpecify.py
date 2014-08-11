__author__ = 'eddie'

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# CallID is the original text message (without time) without spaces

"""
Mogno needed:
    TWIMLS      : {_id: CallID , twiml         : CallTwiml                             }
    TIMEDSHIT   : {_id: time   , instructions  : Message to be parsed (minus time)     }
"""

@app.route('/')
def test_working():
    print "Flask is up and running"

@app.route()
def receiveSMS():
    """
    receives an SMS
    1) Checks who its from
        if me: send to parse
        else: forward to you (with number from)
    """

@app.route('/check_schedules_tasks')
def check_scheduled_tasks():
    """
    Checks mongo for scheduled tasks: if so run to parse
    Heroku will run this every 10 mins
    """

@app.route('/call/<call_id>')
def return_TWIML(call_id):
    """
    returns the TWIML for a call ID
    TWIML must already be hosted and stored in Mongo
    """
@app.route('/getrequests')
def return_requests():
    """
    Shows all previous and future calls (FUTURE CALLS SEPERATED)
    """


def sms(number, SMStext):
    """
    Sends an SMS with the given text to the number
    """


def parse(instructions):
    """
    First: test for time requests (delimted by  #16:00):
        takes message without timing and saves it to timed request ####
    Parses for:
        1) number deliminated by +
        2) message delimiated by :
        3) options deliminated by -
    option default to -t which is a text:
    other option is:
        -c (call)
            f (female)
            ? (record)
    """


def call(number, message_url):
    pass

