# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 22:15:30 2023

@author: User
"""

import matplotlib.pyplot as plt

plt.figure(figsize = [8,8],
           dpi = 96,
           facecolor = 'whitesmoke',
           edgecolor = 'r',
           linewidth = 1,
           frameon = True)
plt.subplot(2,2,1)
plt.title('chart 1')
plt.plot([1, 2, 3], 'k-.o')
plt.subplot(2,2,2)
plt.title('chart 2')
plt.plot([1, 2, 3], 'r:p')
plt.subplot(2,2,3)
plt.title('chart 3')
plt.plot([1, 2, 3], 'g--d')
plt.subplot(2,2,4)
plt.title('chart 4')
plt.plot([1, 2, 3], 'y-.*')

plt.show()