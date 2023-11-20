# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:09:25 2023

@author: User
"""

import matplotlib.pyplot as plt
year = [2016, 2017, 2018, 2019, 2020]
city1 = [128, 150, 199, 180, 150]
city2 = [120, 145, 180, 170, 120]
plt.plot(year, city1, 'm-.^', lw = 2, ms = 10, label = 'Taipei' )
plt.plot(year, city2, 'c--d', lw = 2, ms = 10, label = 'Tainan')
plt.legend()
plt.ylim(50, 250)
plt.xticks(year)
plt.title('sales report', fontsize = 18)
plt.xlabel('year', fontsize = 12)
plt.ylabel('million', fontsize = 12)
plt.grid(color = 'k', lw = 1, alpha = 0.5, ls =':')
plt.tick_params(axis= 'both', labelsize = 14, color = 'r')
plt.show()