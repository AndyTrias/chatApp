from flask import Blueprint, flash, render_template, redirect, request, session, url_for
from flask_login import login_required,  login_user, logout_user, current_user
from chatapp.models import User, db
from chatapp.helpers import send_message, add_user, delete_user

views = Blueprint("views", __name__)


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

        else:
            if send_message(phone):
                session["id"] = user.id
                session["opportunities"] = 1
                return redirect(url_for("views.verify"))

    return render_template("log.html", user=current_user)


# User Log in
@views.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        phone = request.form.get("phone")
        name = request.form.get("name")
        user = add_user(name=name, phone=phone)

        if send_message(phone):
            session["id"] = user.id
            session["opportunities"] = 1
            return redirect(url_for("views.verify"))

        else:
            delete_user(user)

    return render_template("register.html", user=current_user)


@views.route("/verify", methods=["GET", "POST"])
def verify():
    new_user = False
    try:
        if session["id"]:
            new_user = User.query.get(session["id"])
    finally:
        if not new_user:
            return redirect(url_for("views.register"))

    if request.method == "POST":
        if session["pin"] == request.form.get("pin"):
            new_user.active = True
            db.session.commit()
            session.clear()
            login_user(new_user, remember=True)
            return redirect(url_for("views.index"))

        elif session["opportunities"] == 5:
            session.pop("opportunities")
            session.pop("pin")
            flash("Too many opportunities missed. Try again and a new pin will be sent", "error")

            if new_user.is_active():
                return redirect(url_for("views.log"))

            else:
                delete_user(new_user)
                return redirect(url_for("views.register"))

        else:
            flash("Invalid Pin. Try again", "error")
            session["opportunities"] += 1

    return render_template("verify.html", user=current_user)


@views.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.log"))
