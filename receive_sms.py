#!/usr/bin/env python3
import MySQLdb as mdb
from flask import Flask, request, redirect
from process_response import reply, isNewUser
from userStates import OFF, NEW_USER, EXISTING_USER, CATEGORY_INPUT, GETTING_CATEGORY, ADDING_USER
from db_functions import get_user_state, driver


app = Flask(__name__)

# Current User State
STATE = ""

@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    fromNumber = request.values.get('From', None)
    body = request.values.get('Body', None)
    # Check new user
    if isNewUser(fromNumber):
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

def getState(phoneNumber):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        return str(get_user_state(phoneNumber, cur))

if __name__ == "__main__":
    try:
        app.run(debug=True, port=8080)
    except Exception as err:
        print(err)
    finally:
        driver.close()
