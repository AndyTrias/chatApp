from flask import Blueprint, flash, render_template, redirect, request, session, url_for
from flask_login import login_required, login_user, logout_user, current_user
from chatapp.models import User, Contact, Message, MessageRecipient
from chatapp.helpers import send_message, add_user, add_contact, get_user, delete_user

views = Blueprint("views", __name__)


# Login required redirects to register
@views.route("/")
@login_required
def index():
    return render_template("index.html", user=current_user)


@views.route("/chat", methods=["GET", "POST"])
@login_required
def chat():
    contact_id = request.form.get("contact")
    contact = Contact.query.get(contact_id)

    if contact:
        # Tried to replicate the following sql query

        # Get messages sent from user to contact
        # SELECT content
        # FROM message WHERE sender_id = current_user.id and
        # id IN(SELECT message_id FROM message_recipient WHERE receiver_id = contact.id);

        # Get messages sent from contact to user
        # SELECT content
        # FROM message WHERE sender_id = contact.id and
        # id IN(SELECT message_id FROM message_recipient WHERE receiver_id = current_user.id);

        messages = Message.query.filter((Message.sender_id == current_user.id) &
                                        (Message.message_recipient.has(MessageRecipient.receiver_id == contact.id)))

        messages = messages.union(Message.query.filter((Message.sender_id == contact.id) &
                                                       (Message.message_recipient.has(
                                                        MessageRecipient.receiver_id == current_user.id))))

        # Send to client contact, user and messages
        return render_template('chat.html', contact=contact, user=current_user, messages=messages)

    flash("Contact not found", "error")
    return redirect(url_for("views.index"))


@views.route("/contacts", methods=["GET", "POST"])
@login_required
def add_contacts():
    if request.method == "POST":
        phone = request.form.get("phone")
        name = request.form.get("name")
        contact_user = get_user(phone)

        # Check if user exists
        # Check if user is not already a contact
        if contact_user:
            if Contact.query.filter_by(user_id=current_user.id, contact_id=contact_user.id).first():
                flash("User is already a contact", "error")

            else:
                add_contact(user=current_user.id, phone=phone, contact_name=name)

        else:
            flash("No user found with this phone", "error")

    return render_template("addContact.html")


@views.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    if request.method == "POST":
        contact_id = request.form.get("contact")
        contact = Contact.query.get(contact_id)

        if contact:
            delete_user(contact)

        else:
            flash("Contact not found", "error")

    return render_template("delete.html", contacts=Contact.query.filter_by(user_id=current_user.id).all())


@views.route("/log", methods=["GET", "POST"])
def log():
    if request.method == "POST":
        phone = request.form.get("phone")
        user = get_user(phone)

        if user:
            # Check if phone was valid for messages
            if send_message(phone):
                # Store id in sessions to avoid wrong redirections to verify
                session["id"] = user.id
                return redirect(url_for("views.verify"))

        else:
            flash("No user found with this phone or it was unable to send a message", "error")

    return render_template("log.html", user=current_user)


@views.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        phone = request.form.get("phone")
        name = request.form.get("name")

        # Phone must be unique
        if get_user(phone):
            flash("Phone already registered. Please log in", "error")
            return redirect(url_for("views.log"))

        # Add user to database once message has been sent
        # Store id in sessions to avoid wrong redirections to verify
        if send_message(phone):
            user = add_user(name=name, phone=phone)
            session["id"] = user.id
            return redirect(url_for("views.verify"))

    return render_template("register.html", user=current_user)


@views.route("/verify", methods=["GET", "POST"])
def verify():
    # Make sure user has been correctly redirected
    # If not redirect to register
    if session.get("id"):
        new_user = User.query.get(session["id"])
    else:
        return redirect(url_for("views.register"))

    if request.method == "POST":
        session["opportunities"] = 1
        if session["pin"] == request.form.get("pin"):
            session.clear()
            login_user(new_user, remember=True)
            return redirect(url_for("views.index"))

        flash("Invalid Pin. Try again", "error")
        session["opportunities"] += 1

        # Clear pin and opportunities. Let user try again
        if session["opportunities"] == 5:
            session.clear()
            flash("Too many opportunities missed. Try again and a new pin will be sent", "error")
            return redirect(url_for("views.log"))

    return render_template("verify.html", user=current_user)


# Uses flask log in module
@views.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.log"))
