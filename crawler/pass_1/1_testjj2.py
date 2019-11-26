import requests
from bs4 import BeautifulSoup

url = 'https://spidermen.cn'
res = requests.get(url)

soup = BeautifulSoup(res.text,'html.parser')
items = soup.find_all('header',class_='entry-header')

for item in items:
    title = item.find('h2')
    time = item.find('time')
    href = item.find('a',rel='bookmark')
    print('标题：' + title.text + '时间：' + time.text + '链接：' + href['href'])