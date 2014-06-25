__author__ = 'DT'


import os
from flask import Flask, request, redirect
import twilio
from twilio import twiml
from twilio.rest import TwilioRestClient


#ACCOUNT_SID = "ACd44d711fa3867cbb1d77184dc48a69b2"
#AUTH_TOKEN = "79f744af5e9e19fae4215c4a4b602flf"
ACCOUNT_SID = "ACbdc62d802802d2191bdf844bfd208461"
AUTH_TOKEN = "8238ad2b6e2bdd428391914b780fc5c4"
T_NUM = '+18602375985'
E_NUM = '+16304733343'
CALLERS = {
        "+18604605536": "Thomas",
        "+18609176080": "James",
        "+19802970490": "Miles"
}
DEBUG_DICTIONARY = []

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    resp = twilio.twiml.Response()
    resp.say("Hello, we appreciate your call and will get back to you as soon as possible.")
    return str(resp)

@app.route('/7Boyden', methods=['GET', 'POST'])
def receiveSMS():
    from_num = request.values.get('From', None)
    incMessage = request.values.get('Body')
    if (from_num) in CALLERS:
        caller = CALLERS[from_num]
    else:
        caller = "Nemo"
    sms([from_num], "Hello " + caller)
    # Say a command, and listen for the caller to press a key. When they press
    # a key, redirect them to /handle-key.
    # with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
    #     g.say("To speak to a real person, press 1. Press any other key to start over.")
    #resp = twilio.twiml.Response()
    #resp.message(incMessage)

@app.route('/13Oak', methods=('GET', 'POST'))
def receiveCall():
    from_num = request.values.get('From', None)
    if (from_num) in CALLERS:
        caller = CALLERS[from_num]
    else:
        caller = "Nemo"
    resp = twilio.twiml.Response()
    resp.say("Hello, " + caller)
    with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
        g.say("To speak to a real person, press 1. Press any other key to start over.")
    return str(resp)



@app.route('/handle-key', methods=['GET', 'POST'])
def handle():
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        resp = twilio.twiml.Response()
        resp.say("Thank you for pressing 1")
        return str(resp)
    if digit_pressed == "2":
        return redirect("/conference")
    else:
        return redirect("/13Oak")

@app.route('/Debug')
def deb():
    return str(DEBUG_DICTIONARY)

@app.route('/conference', methods=['GET', 'POST'])
def con():
    resp = twilio.twiml.Response()
    resp.say("Joining the conference.")
    lounge = twilio.twiml.Conference()
    resp.dial(lounge)
    return str(resp)

def sms(Numbers, Body):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        to=Numbers[0],
        from_=T_NUM, #Twilio number
        body=Body, #Body is Str of message NOT TWIML
    )
    print message.sid


def call(Numbers):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    call = client.calls.create(to=Numbers[0],  # Any phone number
                           from_=T_NUM, # Must be a valid Twilio number
                           url="http://obscure-savannah-9638.herokuapp.com/")

#def receive(From, To, Body):
 #   pass
# a = ["+18604605536", "+19802970490", "+18603264336"]
# SMS(a, "Yo this is Steve. Pumped to get in tomorrow let's throw a banger.")

#if __name__ == "__main__":


    ''' message.replace("<Say>", "<Response><Say>")
        message.replace("</Say>", "</Response></Say>")
    '''