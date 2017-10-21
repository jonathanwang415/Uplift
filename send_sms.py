#!/usr/bin/env python3
from twilio.rest import Client

# Your Account SID from twilio.com/console
from constants import ACCOUNT_SID, AUTH_TOKEN


def send_message(message, to_number):
    '''Send a message using twilio.'''
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # This sends the text message
    message = client.messages.create(
        to=to_number,  # Number you are sending it to
        from_="+15174814216",  # Our registered Twilio number
        body=message)  # The messsage we are sending
    return message.sid


if __name__ == '__main__':
    send_message('Hello', '+17146235999')
