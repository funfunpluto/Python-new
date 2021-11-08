#! /usr/local/bin/python3

# https://www.learndatasci.com/tutorials/python-finance-part-2-intro-quantitative-trading-strategies/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid', context='talk', palette='Dark2')

#read saved pickle file and display the top 10 records
data = pd.read_pickle('stock.pkl')
print(data.head(10)) 

short_rolling = data.rolling(window=20).mean()
long_rolling = data.rolling(window=100).mean()
print(long_rolling.tail())


