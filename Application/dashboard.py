from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Application.auth import login_required
from Application.db import get_db

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard',methods=('GET', 'POST'))
@login_required
def dashboard():
    # CHECK CREDENTIALS
    return render_template('user/dashboard.html')