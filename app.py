from flask import Flask, render_template
import json
import sys
sys.path.append('src')
from utils import jsonParser
import pandas as pd
import numpy as np

with open("data/json-converted/assignment-1/1-tsv-to-json.json") as f:
    j1 = json.loads(f.read())['Email']
    json_1 = json.dumps(jsonParser(j1))

with open("data/json-converted/assignment-2/2-tsv-to-json.json") as f:
    j2 = json.loads(f.read())['Email']
    json_2 = json.dumps(jsonParser(j2))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vis1')
def vis1():
    df = pd.DataFrame(json.loads(json_1))
    df['location'].replace('', np.nan, inplace=True) # drop empty strings
    # print(df.dropna()['location'])
    json_data = df.dropna()['location'].to_json(orient='values')
    json_data = json.loads(json_data)
    json_data = [i for i in json_data if type(i) == list ] # remove string values

    # sometimes the data is not in correct format, like [xx.xxxx, -xx.xxxx]. If so, change it to dict.
    for i, loc in enumerate(json_data):
        if type(loc[0]) != dict:
            loc_new = [{"lat": loc[0], "lng": loc[1]}] 
            json_data[i] = loc_new

    return render_template('vis1.html', json=json_data)

if __name__ == '__main__':
    app.run(debug=True)