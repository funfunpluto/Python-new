#! /usr/local/bin/python3
#https://www.learndatasci.com/tutorials/python-finance-part-yahoo-finance-api-pandas-matplotlib/

import pandas_datareader.data as web
from datetime import datetime
import pandas as pd


#import matplotlib.finance as mpf
import matplotlib.pyplot as plt

start = datetime(2015, 2, 9)
end = datetime(2017, 5, 24)

tickers = ['AAPL', 'MSFT', '^GSPC']

#get single stock data
gl = web.DataReader('goog', 'yahoo', start, end)

#get a group of stocks from website to dataframe
ff = web.DataReader(tickers, 'yahoo', start, end)


#print(gl.head())

#h = panel_data.to_frame()
ff.head()

# Getting only closing prices
close = ff['Close']
#print(close)

#getting all wekdays: B
#
#Freq code: https://pandas.pydata.org/pandas-docs/stable/timeseries.html#timeseries-offset-aliases
all_weekdays = pd.date_range(start=start, end=end, freq='B')
close_align = close.reindex(all_weekdays)

#fill in all the NA
closef = close_align.fillna(method='ffill')
closef.to_pickle('stock.pkl')

#top 10 records
closef.head(10)

#summary of values
print(closef.describe())

#plot apple time-series(calculated by taking for each date the average of last couple (W) of prices)
#rolling for a number of days

#returns a Panda series object indexed by date
aapl = closef.loc[:, 'AAPL']
short_rolling_aapl = aapl.rolling(window=20).std()
long_rolling_aapl = aapl.rolling(window=200).std()
