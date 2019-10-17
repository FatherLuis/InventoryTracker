from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('contract', __name__)

@bp.route('/contract',methods=('GET', 'POST'))
def contract():
    # CHECK CREDENTIALS
    return render_template('contract/contract.html')