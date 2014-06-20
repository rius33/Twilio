__author__ = 'DT'


import os
from flask import Flask, request
import twilio
from twilio.rest import TwilioRestClient


# ACCOUNT_SID = "ACd44d711fa3867cbb1d77184dc48a69b2"
# AUTH_TOKEN = "79f744af5e9e19fae4215c4a4b602flf"
ACCOUNT_SID = "ACbdc62d802802d2191bdf844bfd208461"
AUTH_TOKEN = "8238ad2b6e2bdd428391914b780fc5c4"
T_NUM = '+18602375985'
E_NUM = '+16304733343'

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/james')
def he():
    return 'Well Hi James!'

@app.route('/miles')
def h():
    return 'Fuck You Miles!'

def SMS(Numbers, Body):
    # Download the Python helper library from twilio.com/docs/python/install
    for number in Numbers:
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=Body, #Body is Str of message NOT TWIML
            to=number,
            from_=E_NUM, #Twilio number
        )
        print message.sid

@app.route('/17_Nauyaug', methods = ['GET', 'POST'])
def receive1():
    from_num = request.values.get('From', None)
    incMessage = request.values.get('Body')

    SMS('+18603264336', incMessage)
    resp = twilio.twiml.Response()
    resp.message(incMessage)

    return str(resp)



def receive(From, To, Body):
    pass
# a = ["+18604605536", "+19802970490", "+18603264336"]
# SMS(a, "Yo this is Steve. Pumped to get in tomorrow let's throw a banger.")