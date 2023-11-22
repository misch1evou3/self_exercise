# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:29:19 2023

@author: User
"""
import csv
import time
import requests
from bs4 import BeautifulSoup

url = 'https://search.books.com.tw/search/query/key/%E6%BC%94%E7%AE%97%E6%B3%95/cat/all'

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
           'AppleWebKit/537.36 (KHTML, like Gecko)'
           'Chrome/110.0.5481.104 Saari/537.36'}

def parse_html(r):
    if r.status_code == requests.codes.ok:
        r.encoding = 'utf8'
        soup = BeautifulSoup(r.text, 'lxml')
    else:
        print("HTTP請求錯誤..." + url)
        soup = None
    return soup

def save_to_csv(items, file):
    with open(file, 'w+', newline='', encoding='utf-8-sig') as fp:
        writer = csv.writer(fp)
        for item in items:
            writer.writerow(items)
            
def web_scraping_bot():
    booklist = [['書名','網址','書價']]
    print("抓取網路資料中...")
    soup = parse_html(requests.get(url, headers = headers))
    if soup != None:
        tag_item = soup.find_all(class_='table-td')
        for item in tag_item:
            book = []
            book.append(item.find('img')['alt'])
            book.append('http:' + item.find('a')['href'])
            price = item.find(class_='price').find_all('b')
            if len(price) == 1:
                book.append(price[0].string)
            else:
                book.append(price[1].string)
            print(book)
            booklist.append(book)
            time.sleep(2)
    return booklist

if __name__ == '__main__':
   booklist = web_scraping_bot()
   for item in booklist:
       print(item)
   save_to_csv(booklist, 'booklist.csv')