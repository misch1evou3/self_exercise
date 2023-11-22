# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:19:31 2023

@author: User
"""

import time 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--disable-notificaitons')



chrome_driver_path = r'C:\Users\User\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe'  
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://www.facebook.com/nchumis')
time.sleep(5)

exit_btn = driver.find_element(By.XPATH,
                               '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div')
exit_btn.click()

for x in range(1,4):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)
    
soup = BeautifulSoup(driver.page_source, 'lxml')

titles = soup.find_all('span',{'class': 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h'})

i = 1
for title in titles:
    post = title.find('div', {'dir':'auto'})
    if post:
        print('第{}篇貼文第一行內容為:{}'.format(i, post.getText()))
        i += 1
        
driver.quit()