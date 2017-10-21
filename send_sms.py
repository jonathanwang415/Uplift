from twilio.rest import Client

# Your Account SID from twilio.com/console
from constants import account_sid, auth_token

client = Client(account_sid, auth_token)

# This sends the text message
message = client.messages.create(
    to="", # Number you are sending it to
    from_="+15174814216", # Our registered Twilio number
    body="Hello from Python!") # The messsage we are sending

print message.sid
