__author__ = 'DT'


import os
from flask import Flask, request, redirect, url_for
import twilio
from twilio import twiml
from twilio.rest import TwilioRestClient

ACCOUNT_SID = "ACbdc62d802802d2191bdf844bfd208461"
AUTH_TOKEN = "8238ad2b6e2bdd428391914b780fc5c4"
T_NUM = '+18602375985'
E_NUM = '+16304733343'
CALLERS = {
        "+18604605536": "Thomas",
        "+18609176080": "James",
        "+19802970490": "Miles",
        "+18603264336": "Tim",
        "+16462563954": "Eddie"
}
DEBUG_DICTIONARY = []

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return 'Hello World.'

@app.route("/call/<call_body>", methods=['GET', 'POST'])
def basic(call_body):
    resp = twilio.twiml.Response()
    resp.say(call_body)
    return str(resp)

@app.route('/7Boyden', methods=['GET', 'POST'])
def receiveSMS():
    from_num = request.values.get('From', None)
    body = request.values.get('Body')
    directions = body.split(':')
    if CALLERS[from_num] == "Tim":
        if directions[0] == "-m":
            sms([directions[1]], directions[2])
        elif directions[0] == "-c":
            call([directions[1]], directions[2])
        else:
            sms(["+18603264336"], body)
    else:
        sms(["+18603264336"], str(from_num) + " " + body)

@app.route('/13Oak', methods=('GET', 'POST'))
def receiveCall():
    from_num = request.values.get('From', None)
    if (from_num) in CALLERS:
        caller = CALLERS[from_num]
    else:
        caller = "Nemo"
    resp = twilio.twiml.Response()
    resp.say("Hello, " + caller, voice="woman")
    with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
        g.say("To speak to Tim, press 1. To access the conference line, press 2.", voice="woman")
    return str(resp)

@app.route('/handle-key', methods=['GET', 'POST'])
def handle():
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        str = "<?xml version='1.0' encoding='UTF-8'?><Response>"
        str += "<Say>Connecting you to Tim. Please hold.</Say>"
        str += "<Dial><Number url='/screen'>+18603264336</Number></Dial></Response>"
        return str
    if digit_pressed == "2":
        return redirect("/conference")
    else:
        return redirect("/13Oak")

@app.route('/screen', methods=['GET', 'POST'])
def screencall():
    str = "<?xml version='1.0' encoding='UTF-8'?><Response>"
    str += "<Gather action='handle-screen' numDigits='1'><Say>To accept this call, press 1.</Say>"
    str += "<Say>To decline this call, press any other number.</Say></Gather>"
    str += "<Say>Sorry, your response was lost in translation.</Say><Redirect>'/screen'</Redirect></Response>"
    return str

@app.route('/handle-screen', methods=['GET', 'POST'])
def decide():
    digit_pressed = request.values.get('Digits', None)
    str = "<?xml version='1.0' encoding='UTF-8'?><Response>"
    if digit_pressed == "1":
        str += "<Say>Connecting you to the caller</Say>"
    else:
        str += "<Hangup />"
    str += "</Response>"
    return str

@app.route('/debug')
def deb():
    return str(DEBUG_DICTIONARY)

@app.route('/conference', methods=['GET', 'POST'])
def con():
    num = request.values.get('From', None)
    str = "<?xml version='1.0' encoding='UTF-8'?><Response><Say>"
    if (CALLERS[num] == "Tim"):
        str += "Joining the conference as a moderator.</Say><Dial><Conference startConferenceOnEnter='true' "
        str += "endConferenceOnExit='true'>Lounge</Conference></Dial><Say>You</Response>"
        return str
    elif (num in CALLERS):
        str += "Joining the conference as a speaker.</Say><Dial><Conference startConferenceOnEnter='false'>Lounge" \
               "</Conference></Dial><Say>The conference has ended. Thank you for attending.</Say></Response>"
        return str
    else:
        str += "Joining the conference as a listener.</Say><Dial><Conference startConferenceOnEnter='false' muted='tr" \
               "ue'>Lounge</Conference></Dial><The conference has ended. Thank you for listening.</Say></Response>"
        return str

def sms(Numbers, Body):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    for number in Numbers:
        message = client.messages.create(
            to=number,
            from_=T_NUM, #Twilio number
            body=Body, #Body is Str of message NOT TWIML
        )
    print message.sid


def call(Numbers, Body):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    call = client.calls.create(to=Numbers[0],  # Any phone number
                           from_=T_NUM,
                           url="http://obscure-savannah-9638.herokuapp.com" + url_for('basic', call_body=Body))

# if __name__ == "__main__":
#    call(["+18603264336"], "Fuck you.")


# ''' message.replace("<Say>", "<Response><Say>")
#         message.replace("</Say>", "</Response></Say>")
# '''