import requests
from bs4 import BeautifulSoup
res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
html = res.text
soup = BeautifulSoup( html,'html.parser')
it = soup.find(id='recentcomments')
items = it.find_all(class_='recentcomments')
for item in items:
    print(item.text)