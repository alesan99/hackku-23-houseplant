import functools
import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from project.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('auth.quiz'))

        flash(error)

    return render_template('auth/login.html')



@bp.route('/quiz', methods=('GET','POST'))
@login_required
def quiz():
    with open("./project/templates/auth/quiz.json") as f:
        var = json.load(f)
        id = session['user_id']
        if request.method == 'GET':
            db = get_db()
            error = None
            user = db.execute(
                'SELECT * FROM quiz WHERE user_id = ?', (id,)
            ).fetchall()
        elif request.method == "POST":
            db = get_db()
            error = None
            user = db.execute(
                'DELETE FROM quiz WHERE user_id = ?', (id,)
            ).fetchall()
            for y in range(3):
                b = "q"+str(y)
                x = float(request.form[b])
                for i in range(6):
                    if i == x and i==1:
                        x = (x*0)
                    if i == x and i==2:
                        x = (x*.25)
                    if i == x and i==3:
                        x= (x*.50)
                    if i == x and i==4:
                        x==x*.75
                    if i == x and i==5:
                        x=x*1
                quiz_answer = x
                try:
                    db.execute(
                    "INSERT INTO quiz (qustion_answer,user_id) VALUES (?, ?)",
                    (quiz_answer,id),
                    )
                    db.commit()
                except db.IntegrityError:
                    error = "INTERROR"
            
            
            '''if user_count< 2:
                error = 'Please check all answers.'''
            
            if error is not None:
                flash(error)

            return redirect(url_for('home'))
        return render_template('auth/quiz.html', user = user,questions = var["Quiz"])


    #return render_template('auth/index.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@bp.route('/results')
def results():
    with open("./project/templates/auth/quiz.json") as f:
        var = json.load(f)
        db=get_db()
        id = session['user_id']
        user_type = db.execute(
            'SELECT id FROM user WHERE user_id = ?', (id,)
            ).fetchall()
        

    return