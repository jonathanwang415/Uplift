#!/usr/bin/env python3
import MySQLdb as mdb
from flask import Flask, request, redirect
from process_response import reply
from userStates import OFF, NEW_USER, EXISTING_USER, CATEGORY_INPUT, SIGN_UP, TIME_INPUT
from db_functions import get_user_state


app = Flask(__name__)

# Current User State
STATE = ""

@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    fromNumber = request.values.get('From', None)
    body = request.values.get('Body', None)
    # Check new user
    STATE = getState(fromNumber)
    reply(fromNumber, body, STATE)


    # Other fields we could leverage later on
    # direction = request.values.get('Direction', None)
    # city = request.values.get('FromCity', None)
    # state = request.values.get('FromState', None)
    # zip = request.values.get('FromZip', None)
    # country = request.values.get('FromCountry', None)

def getState (phoneNumber):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        return str(get_user_state(phoneNumber, cur))

if __name__ == "__main__":
    app.run(debug=True)
