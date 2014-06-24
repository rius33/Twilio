__author__ = 'DT'

from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACbdc62d802802d2191bdf844bfd208461"
AUTH_TOKEN = "8238ad2b6e2bdd428391914b780fc5c4"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

for call in client.calls.list():
    print "From: " + call.from_formatted + " To: " + call.to_formatted