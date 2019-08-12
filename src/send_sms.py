# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def sendSms(phone):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC050daa6410a7d71aa3266c8bd22cbdfa'
    auth_token = '821ccca07308bd4f91233471c921e8ed'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_='+19384440856',
                        to=phone
                    )

    print(message.sid)
