import requests
from bs4 import BeautifulSoup

url = 'http://www.xiachufang.com/explore'
res = requests.get(url)

soup = BeautifulSoup(res.text,'html.parser')
items = soup.find_all('div',class_='info pure-u')

for item in items:
    name_a = item.find('p',class_='name')

    name = name_a.find('a')
    zhuliao_p = item.find('p',class_='ing ellipsis')
    zhuliao = zhuliao_p.find_all('a')
    
    listz = []
    for i in zhuliao:
        listz.append(i.text)
    
    print('名字' + name.text + '链接：' + url+str(name['href']) + '主料：' + str(listz[:] ))

