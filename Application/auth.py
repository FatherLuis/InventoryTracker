from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('auth', __name__)

@bp.route('/',methods=('GET', 'POST'))
def login():
    # CHECK CREDENTIALS
    return render_template('auth/login.html')