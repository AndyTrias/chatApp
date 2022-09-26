import secrets
import os
from . import db
from .models import User
from twilio.rest import Client
from twilio.base import exceptions
from flask import session, flash


def get_user(phone):
    return User.query.filter_by(phone=phone).first()


def delete_user(user):
    db.session.delete(user)
    db.session.commit()


# Send a message using twilio library
# Uses twilio free development number
def send_message(phone):
    pin = "{:0>4}".format(secrets.randbelow(10 ** 4))

    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
                                        body=f"your verification code is {pin}",
                                        from_=os.environ["TWILIO_PHONE_NUMBER"],
                                        to=phone
                                        )
    except exceptions.TwilioRestException as e:
        if "HTTP 400" in str(e):
            print(phone, str(e))
            flash("Invalid number. Try again", "error")
            flash("Remember phone number must be verified in Twilio", "error")
            return False

        else:
            raise e

    # Store pin in sessions to use it in verify
    session["pin"] = pin
    return True
