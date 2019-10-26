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
    
    db = get_db()
    semester = [x[0] for x in db.execute("SELECT [SemesterName] FROM [Semester]").fetchall()]
    course = [x[0] for x in db.execute("SELECT [CourseName] FROM [Course]").fetchall()]
    professor = [x[0] for x in db.execute("SELECT Person.FirstName || ' ' || Person.LastName AS name FROM [Person] JOIN [Professor] ON [Professor].PersonID = [Person].PersonID").fetchall()]


    if request.method == "POST":

        if 'cancel' in request.form:
            return redirect(url_for("dashboard.dashboard"))
        elif 'submit' in request.form:
            return 'Happy'


    return render_template('contract/contract.html',semesters = semester,courses=course,professors=professor)
