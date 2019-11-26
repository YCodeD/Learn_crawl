# import requests

# res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
# music = res.content
# file = open('music.mp3','wb')
# file.write(music)
# file.close()

# import requests
# res = requests.get('https://localprod.pandateacher.com/python-manuscript//crawler-html/spider-men5.0.html')
# text = res.text
# file = open('这个书苑不太冷5.0.txt', 'a', encoding='utf-8')
# file.write(text)
# file.close()

import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('http://www.xiachufang.com/explore/')
# 获取数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 解析数据
list_foods = bs_foods.find_all('div',class_='info pure-u')
# 查找最小父级标签

tag_a = list_foods[0].find('a')
# 提取第0个父级标签中的<a>标签
print(tag_a.text[17:-13])
# 输出菜名，使用[17:-13]切掉了多余的信息
print('http://www.xiachufang.com'+tag_a['href'])
# 输出URL