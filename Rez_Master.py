__author__ = 'DT'

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/james')
def he():
    return 'Well Hi James!'

@app.route('/miles')
def h():
    return 'Fuck You Miles!'