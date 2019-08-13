import os
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def sendSms(phone):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = os.environ.get('ACCOUNTSID')
    auth_token = os.environ.get('TWILIOTOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Your turn!",
                        from_='+19384440856',
                        to=phone
                    )

    print(message.sid)
