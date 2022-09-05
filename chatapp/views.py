from flask import Blueprint, flash, render_template, redirect, request, session, url_for
from flask_login import login_required,  login_user, logout_user, current_user
from chatapp.models import User, db
from chatapp.helpers import send_message, add_user

views = Blueprint("views", __name__)

# Login required redirects to register


@views.route("/")
@login_required
def index():
    return render_template("index.html", user=current_user)


@views.route("/log", methods=["GET", "POST"])
def log():
    if request.method == "POST":
        phone = request.form.get("phone")
        user = User.query.filter_by(phone=phone).first()

        if user is None:
            flash("No user found with this phone", "error")

        # Store id in sessions to avoid wrong redirections to verify
        else:
            if send_message(phone):
                session["id"] = user.id
                return redirect(url_for("views.verify"))

    return render_template("log.html", user=current_user)


@views.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        phone = request.form.get("phone")
        name = request.form.get("name")

        # Phone must be unique
        if User.query.filter_by(phone=phone).first():
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
