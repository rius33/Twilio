__author__ = 'DT'


import os
from flask import Flask, request
import twilio
from twilio import twiml
from twilio.rest import TwilioRestClient


#ACCOUNT_SID = "ACd44d711fa3867cbb1d77184dc48a69b2"
#AUTH_TOKEN = "79f744af5e9e19fae4215c4a4b602flf"
ACCOUNT_SID = "ACbdc62d802802d2191bdf844bfd208461"
AUTH_TOKEN = "8238ad2b6e2bdd428391914b780fc5c4"
T_NUM = '+18602375985'
E_NUM = '+16304733343'
DEBUG_DICTIONARY = []

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/abc', methods = ['GET', 'POST'])
def receive():
    from_num = request.values.get('From', None)
    incMessage = request.values.get('Body')
    resp = twilio.twiml.response()
    resp.say("Hello Tim.")
    return str(resp)
    #sms([from_num], incMessage)
    #call([from_num])
    #DEBUG_DICTIONARY.append(from_num)
    #DEBUG_DICTIONARY.append(incMessage)
    #resp = twilio.twiml.Response()
    #resp.message(incMessage)
    #DEBUG_DICTIONARY.append(str(resp))
    #sms([from_num], incMessage)
    #return str(resp)

#@app.route('/Debug')
#def deb():
#    return str(DEBUG_DICTIONARY)


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
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

#def receive(From, To, Body):
 #   pass
# a = ["+18604605536", "+19802970490", "+18603264336"]
# SMS(a, "Yo this is Steve. Pumped to get in tomorrow let's throw a banger.")

#if __name__ == "__main__":
#    call(["+18603264336"])


    ''' message.replace("<Say>", "<Response><Say>")
        message.replace("</Say>", "</Response></Say>")
    '''