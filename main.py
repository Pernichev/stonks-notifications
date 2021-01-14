import pandas as pd #data manipulation and analysis package
from alpha_vantage.timeseries import TimeSeries #enables data pull from Alpha Vantage
import matplotlib.pyplot as plt #if you want to plot your findings
import time
from Logger import getLogger

import datetime

API_KEY = ''
ticker = 'PLUG'

while True:
    
    t = datetime.datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S')
    print("{t}\nChecking price on {ticker}...\n".format(t=t, ticker=ticker))
    #Getting the data from alpha_vantage
    ts = TimeSeries(API_KEY, output_format='pandas')
    data, meta_data = ts.get_intraday(ticker, interval='5min', outputsize='full')

    #We are currently interested in the latest price

    close_data = data['4. close'] #The close data column
    last_price = close_data[0] #Selecting the last price from the close_data column

    target_price = 75

    #Check if you're getting a correct value
    print(data)
    print("Current Price: {last_price} | Target: {target_price}".format(ticker = ticker, last_price = last_price, target_price = target_price)) 

    if last_price >= target_price:
        logger = getLogger()
        logger.error("{ticker} is trading at: {last_price} | Target price: {target_price} ".format(ticker = ticker, last_price = last_price, target_price = target_price))

    print("Sleeping for 8 minutes")

    time.sleep(480)