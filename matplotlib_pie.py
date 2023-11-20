# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 21:40:04 2023

@author: User
"""

import matplotlib.pyplot as plt

sizes = [25, 30, 15, 10]
labels = ['Taipei', 'Taichung', 'Tainan', 'Taitung']
colors = ['r', 'm', 'y', 'c']
explode = [0, 0, 0.25, 0]
plt.pie(sizes,
        labels = labels,
        colors = colors,
        explode = explode, #圓餅凸出部分
        labeldistance = 1.1, #項目標題與圓心距離是半徑的1.1倍
        autopct = '%2.1f%%', #項目百分比的格式(2位整數1位小數)
        pctdistance = 0.6, #百分比文字與圓心的距離是半徑的0.6倍
        shadow = True,
        startangle = 90) #繪圖起始角度(逆時針旋轉)