# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:55:46 2023

@author: User
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties #matplotlib內建的(中文)字型調整模組
from bs4 import BeautifulSoup
import requests


font_prop = FontProperties() #使用內建字型

month, high, low, average = [], [], [], []
url = 'https://www.twse.com.tw/rwd/zh/afterTrading/FMSRFK?date=20230101&stockNo=2330&response=html'
content = requests.get(url).text
sp = BeautifulSoup(content, 'lxml')
datas = sp.select('table')[0]
title = datas.find('div').text.replace(" ","")
rows = datas.select('tbody tr')
for row in rows:
    cols = row.select("td")
    month.append(int(cols[1].text))
    high.append(float(cols[2].text))
    low.append(float(cols[3].text))
    average.append(float(cols[4].text))

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']   #將預設字體更改為微軟正黑體
plt.plot(month, high, 'r-^', lw = 2, label = '最高價')
plt.plot(month, low, 'g-o', lw = 2, label = '最低價')
plt.plot(month, average, 'y-*', lw = 2, label = '加權平均價')
plt.xlabel('月份')
plt.ylabel('股價')
plt.grid(color = 'k', ls = ':', lw = 1, alpha = 0.5)
plt.legend()
plt.title(title, fontproperties = font_prop)  #中文字型顯示標題
plt.show()