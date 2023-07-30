from flask import Flask, render_template
import json
import os
from sorting import *

app = Flask(__name__)

with open('stockdata.json') as f:
    stockdata = json.load(f)
    f.close()


@app.route("/")
def primary():
    return render_template('primary.html', posts = stockdata['stock_info'])

#sorting/better page??? buttons

@app.route("/test")
def test():
    return render_template('test.html')