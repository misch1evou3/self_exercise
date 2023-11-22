# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

grades = {
    'name':['Mike','Sherry','Cindy','John'],
    'math':[80,75,93,86],
    'chinese':[63,90,85,70]
    }
df = pd.DataFrame(grades) #建立表格
df.insert(3, column = 'englsih', value = [88, 72, 74, 98]) #插入表格pd.insert(第n欄,第n欄名稱,第n欄value)
df2 = pd.DataFrame({
    'name':['Henry','Terry'],
    'math':[60,99],
    'chinese':[62,88]
    })
new_df = pd.concat([df,df2], ignore_index=True) #合併表格pd.concat([表格1,表格2],ignore_index=)
df.info()
print(new_df)
