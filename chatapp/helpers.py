import secrets
import os
from . import db
from .models import User, Contacts
from twilio.rest import Client
from twilio.base import exceptions
from flask import session, flash


def add_user(name, phone):
    new_user = User(name=name, phone=phone)
    db.session.add(new_user)
    db.session.commit()

    return new_user


def add_contact(contact_name, phone, user):
    contact_id = User.query.filter_by(phone=phone).first().id
    new_contact = Contacts(name=contact_name, contact_id=contact_id, user_id=user)
    db.session.add(new_contact)
    db.session.commit()

    return new_contact


def get_user(phone):
    return User.query.filter_by(phone=phone).first()


def delete_user(user):
    db.session.delete(user)
    db.session.commit()


# Send a message using twilio library
# Uses twilio free development number
def send_message(phone):
    pin = "{:0>4}".format(secrets.randbelow(10 ** 4))

    account_sid = "AC71bf099f34730d1bc30f878d5ff5e277"
    auth_token = "945013d87ace01e9ccb5c604ea419e1c"
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
                                        body=f"your verification code is {pin}",
                                        from_="3854832060",
                                        to=phone
                                        )
    except exceptions.TwilioRestException as e:
        if "HTTP 400" in str(e):
            print(phone, str(e))
            flash("Invalid number. Try again", "error")
            return False

        else:
            raise e

    # Store pin in sessions to use it in verify
    session["pin"] = pin
    return True

