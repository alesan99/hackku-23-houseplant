import os

from flask import Flask, render_template, redirect,url_for
import pandas as pd

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='houseplant',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def home():
        return render_template("home/landing.html")
    
    @app.route('/registerlogin')
    def to_auth_login():
        return redirect(url_for("auth.login"))
    
    @app.route('/quiz')
    def to_auth_quiz():
        return redirect(url_for("auth.quiz"))
    

    
  
    
    
    
    from . import db, auth

    db.init_app(app)
    app.register_blueprint(auth.bp)
    return app