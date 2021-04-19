from flask import Flask, render_template
import json
import sys
sys.path.append('src')
from utils import jsonParser
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vis4')
def vis4():
    return render_template('vis4.html')

if __name__ == '__main__':
    app.run(debug=True)