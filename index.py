# memo
# pipenv --venv
# Set-ExecutionPolicy RemoteSigned -Scope Process
import os
import sys
import numpy as np
from config import configure_app
from flask import Flask, render_template, request
from flask_login import LoginManager, login_user, logout_user, login_required

from model.user import user_check, users
# from flask.ext.scss import Scss


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def hello():
  return render_template('hello.html')


@app.route('/login', methods=["GET", "POST"])
def login():
  if request.method == 'POST':
    user = request.form.get('user')
    pswd = request.form.get('pass')
    if all([
        user in user_check,
        pswd == user_check[user]['pswd']
      ]):
      user = users.get(user_check[user]['id'])
      login_user(user)
  return render_template('login.html')


@app.route('/mypage')
@login_required
def mypage():
  pass


if __name__ == "__main__":
  configure_app(app)
  app.run(debug=True)
