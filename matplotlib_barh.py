# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 20:56:03 2023

@author: User
"""

import matplotlib.pyplot as plt

xlist = [45, 28, 38, 32, 50]
ylist = ['c', 'c++', 'c#', 'python', 'java']
plt.barh(ylist, xlist, height=0.7, left= 0, color = ['r', 'm', 'c', 'g', 'y'])
plt.title('Total students')
plt.xlabel('Students')
plt.ylabel('Subjects')
plt.show()