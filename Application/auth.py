from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('auth', __name__)

@bp.route('/',methods=('GET', 'POST'))
def login():
    # CHECK CREDENTIALS

    if request.method == "POST":
        error = None

        username = request.form["username"]
        password = request.form["password"]

        #print('u:{} \n p:{}'.format(type(username),type(password)))


        # USE A DATABASE LATER, THIS IS JUST FOR DEVELOPMENT
        if(not(username == 'Joe') or not(password == '1234')):
            error = 'Incorrect Username or Password'

        if error is None:
            #store the user id in a new session and return to the index
            #session.clear()
            #session["user_id"] = user["id"]
            print('REACH')
            return redirect(url_for("dashboard.dashboard"))

        #print('why')
        #flash(error)

    return render_template('auth/login.html')