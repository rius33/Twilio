__author__ = 'DT'

# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Get these credentials from http://twilio.com/user/account
ACCOUNT_SID = "ACbdc62d802802d2191bdf844bfd208461"
AUTH_TOKEN = "8238ad2b6e2bdd428391914b780fc5c4"
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

# Make the call
call = client.calls.create(to="+18603264336",  # Any phone number
                           from_="+18602375985", # Must be a valid Twilio number
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print call.sid
