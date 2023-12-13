from flask import Flask, render_template
import json
import os
from sorted import *

app = Flask(__name__)

with open('stockdata.json') as f:
    stockdata = json.load(f)
    f.close()

stockdata = stockdata["stock_info"]
mergeSort(stockdata, 0, len(stockdata)-1)

@app.route("/")
def primary():
    return render_template('primary.html', stocks = stockdata)

#sorting/better page??? buttons

@app.route("/test")
def test():
    return render_template('test.html')


if __name__ == "__main__":
    print(stockdata)