#!/usr/bin/python

"""
Khyber Sen and Terry Guan
SoftDev1 pd7
HW7 -- Do I Know You
2017-10-04
"""
from __future__ import print_function

import os

__author__ = 'Khyber Sen and Terry Guan'
__date__ = '2017-10-02'

from flask import Flask
from flask import Response
from flask import render_template
from flask import request
from flask import session
from werkzeug.datastructures import ImmutableMultiDict

# noinspection PyUnresolvedReferences
from util.flask_utils import redirect_url

app = Flask(__name__)

users = {'Hello': 'World'}


def br(n):
    # type: (int) -> str
    return '<br>' * n


@app.redirect_from('/')
@app.route('/login')
def login():
    # type: () -> Response
    if 'username' in session:
        return redirect_url(welcome)
    else:
        return render_template('login.jinja2')


@app.route('/auth', methods=['post'])
def authorize():
    # type: () -> Response
    form = request.form
    username = form['username']
    password = form['password']
    if username not in users:
        return render_template('login.jinja2', failed='username')
    if password != users[username]:
        return render_template('login.jinja2', failed='password')
    session['username'] = username
    return redirect_url(welcome)


@app.route('/welcome')
def welcome():
    username = session['username']
    return render_template('welcome.jinja2', username=username, br=br)


@app.route('/logout')
def logout():
    del session['username']
    return redirect_url(login)


if __name__ == '__main__':
    app.debug = True
    app.secret_key = os.urandom(32)
    app.run()