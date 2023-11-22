# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:49:04 2023

@author: User
"""
import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'

headers = {'user-agent':'Mozilla/5.0(Windows NT 10.0; Win64; x64)'
           'AppleWebKit/537.36 (KHTML, like Gecko)'
           'Chrome/110.0.5481.104 Safari/537.36'}

response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find('table',{'data-test':'historical-prices'})

data = []
rows = table.find_all('tr')
for row in rows[1:-1]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)
    
df = pd.DataFrame(data, columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']).dropna()

plt.figure(figsize = (10,6))
plt.plot(df['Close'].astype(float), label = 'Close Price', color = 'b')
plt.title('Yahoo Historical Stock Price (APPL)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(color = 'k', linestyle = ':', linewidth = 1, alpha = 0.5)
plt.legend()
plt.show()