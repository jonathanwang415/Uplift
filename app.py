import genomelink
# from oauth import OAuth
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)


@app.route('/callback')
def callback():
    clientid = 'K2akFUb86npj5QDnommNDsCEw5QuIKqIYQ6Juf6X'
    clientsecret = 'Ht8b9pDdzbAGUKy9NjxxQagZg3Rm9IbsWW41wnRvvwrX2ecdfbs64DmGJy3PrhOWQBFfvYEWjvAxh2xTWFl7hMMtd0MZVrH536iuu98ZOJmAmzB1aoTcmAZ5cKI1tz54'
    callbackurl = 'http://127.0.0.1:5000/callback'

    # The user has been redirected back from the provider to your registered
    # callback URL. With this redirection comes an authorization code included
    # in the request URL. We will use that to obtain an access token.
    print(request.url)
    token = genomelink.OAuth.token(clientid, clientsecret, callbackurl, request_url=request.url)

    # At this point you can fetch protected resources but lets save
    # the token and show how this is done from a persisted token in index page.
    session['oauth_token'] = token
    return str(token)


if __name__ == '__main__':
    # This allows us to use a plain HTTP callback.
    import os
    os.environ['DEBUG'] = "1"
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    # Run local server on port 5000.
    app.secret_key = os.urandom(24)
    app.run(debug=True)
