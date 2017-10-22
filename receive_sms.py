#!/usr/bin/env python3
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from process_response import getReply

app = Flask(__name__)

@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    resp = MessagingResponse()

    body = request.values.get('Body', None)
    print(body)
    response = getReply(body)

    # Other fields we could leverage later on
    # from_num = request.values.get('From', None)
    # direction = request.values.get('Direction', None)
    # city = request.values.get('FromCity', None)
    # state = request.values.get('FromState', None)
    # zip = request.values.get('FromZip', None)
    # country = request.values.get('FromCountry', None)

    resp.message(response)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    