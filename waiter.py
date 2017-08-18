from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, logout_user
from flask.ext.login import login_user
from mock_db_handler import MockDBHelper as DBHelper
from user import User


DB = DBHelper()
app = Flask(__name__)
app.secret_key = '34e3MkXJjBkuBRYjRSzuJOSBMeWRdGWcePCWa3H8/cLnsBsh6Q4eGQWC0A7/SfbkGlTgaf/MGo0Q5HWoGqGciEhY3OTPAsoJPiY'
login_manager = LoginManager(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/account")
@login_required
def account():
    return "You are logged in"


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    user_password = DB.get_user(email)
    if user_password and user_password == password:
        user = User(email)
        login_user(user, remember=True)
        return redirect(url_for('account'))
    return home()


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)

if __name__ == '__main__':
    app.run()
