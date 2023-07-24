from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyBkCc1WY7Yu2BETjmYA6m3jmHYU4Ll5qMI",
  "authDomain": "fir-17f02.firebaseapp.com",
  "projectId": "fir-17f02",
  "storageBucket": "fir-17f02.appspot.com",
  "messagingSenderId": "787139879406",
  "appId": "1:787139879406:web:e62a546ade52375942eeff",
  "measurementId": "G-K9LW85TTZH", "databaseURL":""}


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet.html'))
        except:
            error = "Authentication failed"

    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)

            return redirect(url_for('add_tweet.html'))
        except:
            error = "Authentication failed"

    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)