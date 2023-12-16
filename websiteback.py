from flask import Flask, render_template
import json
import os
from sorted import *

app = Flask(__name__)

with open('stockdata.json') as f:
    stockdata = json.load(f)
    f.close()

stockdata = stockdata["stock_info"]


@app.route("/")
def primary():
    mergeSort(stockdata, 0, len(stockdata)-1, 'PE')
    return render_template('primary.html', stocks = stockdata)

#sorting/better page??? buttons

@app.route("/test")
def test():
    mergeSort(stockdata, 0, len(stockdata)-1, 'Price')
    return render_template('primary.html', stocks = stockdata)


if __name__ == "__main__":
    print(stockdata)