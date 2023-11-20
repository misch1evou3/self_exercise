# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 20:12:21 2023

@author: User
"""
import matplotlib.pyplot as plt

xlist = ['c', 'c++', 'c#', 'python', 'java']
ylist1 = [25, 20, 20, 16, 28]
ylist2 = [20, 8, 18, 16, 22]
plt.bar(xlist, ylist1, width= 0.7, bottom= 0, label = 'boy')
plt.bar(xlist, ylist2, width= 0.7, bottom= ylist1, label = 'girl')
plt.legend() #顯示出label標籤
plt.title('Total students')
plt.xlabel('Subjects')
plt.ylabel('students')
plt.show()
