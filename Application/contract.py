from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Application.auth import login_required
from Application.db import get_db

bp = Blueprint('contract', __name__)

@bp.route('/contract',methods=('GET', 'POST'))
@login_required
def contract():
    # CHECK CREDENTIALS


    if request.method == "POST":

        if 'cancel' in request.form:
            return redirect(url_for("dashboard.dashboard"))
        elif 'submit' in request.form:
            return 'Happy'

    return render_template('contract/contract.html')












    return render_template('contract/contract.html')