#!/usr/bin/env python3
import MySQLdb as mdb
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

from process_response import reply, isNewUser, getState
from userStates import OFF, NEW_USER, EXISTING_USER, CATEGORY_INPUT, GETTING_CATEGORY, ADDING_USER
from db_functions import get_user_state, driver
from send_sms import send_message


app = Flask(__name__)

# Current User State
STATE = ""

@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    fromNumber = request.values.get('From', None)
    body = request.values.get('Body', None)
    # Check new user
    if isNewUser(fromNumber):
        msg = ("Hi there! This is Uplift’s automated chat bot responding. "
               "I’m here to give you some useful insight about your genome as well as some tips to help you be the best you.")
        send_message(msg, fromNumber)
        STATE = NEW_USER
    else:
        STATE = getState(fromNumber)
    return reply(fromNumber, body, STATE)


    # Other fields we could leverage later on
    # direction = request.values.get('Direction', None)
    # city = request.values.get('FromCity', None)
    # state = request.values.get('FromState', None)
    # zip = request.values.get('FromZip', None)
    # country = request.values.get('FromCountry', None)


if __name__ == "__main__":
    try:
        app.run(debug=True, port=8080)
    except Exception as err:
        print(err)
    finally:
        driver.close()
