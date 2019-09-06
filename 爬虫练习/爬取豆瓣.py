import requests
from bs4 import BeautifulSoup
res = requests.get('https://movie.douban.com/top250?start=0&filter=')
soup = BeautifulSoup(res.text,'html.parser')
tag = soup.find('div',class_='article')
li_all = tag.find_all('li')

list_all = []

for key in li_all:
    tag_url = key.find('a')['href']
    tag_order = key.find('em').text
    tag_name = key.find('span',class_='title').text
    tag_quote = key.find('span',class_='inq').text
    tag_num = key.find('span',class_='rating_num').text
    sub_list = [tag_order,tag_name,tag_num,tag_quote,tag_url]
    list_all.append(sub_list)

print(list_all)