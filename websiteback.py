from flask import Flask, render_template
import json
import os

app = Flask(__name__)

with open('stockdata.json') as f:
    stockdata = json.load(f)
    f.close()

@app.route("/")
def primary():
    stockdata = sorted(stockdata['stock_info'], key=lambda x: x['PE'])
    return render_template('primary.html', posts = stockdata)

#sorting/better page??? buttons

@app.route("/test")
def test():
    return render_template('test.html')

@app.route('/test2')
def test2():
    return render_template('pizza.html')