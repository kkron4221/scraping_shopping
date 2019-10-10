#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import urllib.request
import os.path
from selenium.webdriver import Firefox, FirefoxOptions
from bs4 import BeautifulSoup

options = FirefoxOptions()
options.add_argument('-headless')

url = "search_url"
search_word = "search_word"
new_item_array = {}
count = 20

browser = Firefox(options=options)
browser.get(url)

# サイトを検索して結果を配列に格納
# サイトによって書きかえるべし
search_box = browser.find_element_by_id('yschsp')
search_box.clear()
search_box.send_keys(search_word)
search_btn = browser.find_element_by_id('acHdSchBtn')
search_btn.click()
item = browser.find_elements_by_class_name('Product__titleLink')
for i in range(0, 20):
    new_item_array[i] = item[i].text

# jsonファイルが存在するかをチェックする処理
# if(os.path.exists('/home/ricky/anaconda3/shoe_data.json') == False):


with open('your_directory') as f:
    saved_data = json.load(f)

for i in range(0, 21):
    for data_item in saved_data.values():
        if data_item == item[i].text:
            count -= 1
            
if count > 10:
    print("send")
            
new_item_array.update([('count', count)])


# jsonに書き込み
fw = open('shoe_data.json', 'w')
json.dump(new_item_array, fw)


# jsonファイルを開く
# パスを指定していることに注意
# with open('/home/ricky/anaconda3/shoe_data.json') as f:
#     saved_data = json.load(f)
    
for data_item in saved_data.values():
    print(data_item)

