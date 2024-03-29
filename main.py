#
#This is used for scraping data off of Yahoo finance's undervalued large cap premade screener. It will go through Yahoo finance's screener, get all of the stocks within it
# and get data from each of the stocks through Yahoo's website.
#It will save the data into a json file so that the web scraping doesn't happen multiple times.
#

import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv('.env')
import json

#function to get stock data
def get_stock_data(tag):
    r = requests.get('https://finance.yahoo.com/quote/{tag}'.format(tag = tag),headers = headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    sname = soup.find_all('h1', {'class' : 'D(ib) Fz(18px)'})
    sdata = soup.find_all('td', {'class' : 'Ta(end) Fw(600) Lh(14px)'})
    sprice = soup.find_all('fin-streamer', {'class' : 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    if(len(sdata) != 0):     
        PE = sdata[10].text #this gets the value of PE ratio

        #gets current stock price
        stockprice = sprice[0].text.split(',')
        stockprice = "".join(stockprice)


        #cleaning the name and tag
        stockandtag = sname[0].text.split('(')
        stockandtag[0] = stockandtag[0][0:len(stockandtag[0])-1]
        stockandtag[1] = stockandtag[1][0:len(stockandtag[1])-1]

        stocks.append(stock(stockandtag[1],stockandtag[0],PE, stockprice))
        print(stocks[len(stocks)-1].name)
    else:
        print('fail: ' +  stocks[len(stocks)-1].name)

headerdata = os.getenv('HEADERS')

#stock class
class stock:
    def __init__(self, tag, name, PE, price):
        self.tag = tag
        self.name = name
        self.PE = PE
        self.price = price
    def save_to_json(self, filename):
        #placeholder in for error checking for PE
        if self.PE == 'N/A' or self.PE == None:
            self.PE = 100
        dict = {'Tag': self.tag, 'Name': self.name, 'PE': self.PE, 'Price': self.price}
        with open(filename) as f:
            tmp = json.load(f)
            f.close()
        tmp['stock_info'].append(dict)
        with open(filename, 'w') as f:
            f.write(json.dumps(tmp, indent = 2))
            f.close()
        

#this resets the json file so that the updated data can be readded
with open('stockdata.json') as f:
    tmp = json.load(f)
    f.close()

tmp['stock_info'].clear()

with open('stockdata.json', 'w') as f:
    f.write(json.dumps(tmp, indent = 2))
    f.close()

headers = {'User-Agent': headerdata}

stocktags = []

#runs through the screener and gets all the stocks
offset = 0
while(True):
    r = requests.get('https://finance.yahoo.com/screener/predefined/undervalued_large_caps?count=25&offset={number}'.format(number = offset),headers = headers)
    offset += 25
    soup = BeautifulSoup(r.content, 'html.parser')
    stag = soup.find_all('a', {'class': 'Fw(600) C($linkColor)'})
    if(len(stag)== 0):
        break    
    stocktags = stocktags + stag

#gets the stock information
stocks = []    
iteration = 0
for x in stocktags:
        get_stock_data(stocktags[iteration].text)
        iteration+=1

#saves the stock data to json file
for x in stocks:
    print(x.name + ' (' + x.tag + ')  PE: ' + x.PE + '  Price: ' + x.price)
    x.save_to_json('stockdata.json')