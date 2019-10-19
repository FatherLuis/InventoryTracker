from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('contract', __name__)

@bp.route('/contract',methods=('GET', 'POST'))
def contract():
    # CHECK CREDENTIALS


    if request.method == "POST":

        if 'cancel' in request.form:
            return redirect(url_for("dashboard.dashboard"))
        elif 'submit' in request.form:
            return 'Happy'

    return render_template('contract/contract.html')












    return render_template('contract/contract.html')