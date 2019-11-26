import requests
from bs4 import BeautifulSoup

url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
res = requests.get(url)

soup = BeautifulSoup(res.text,'html.parser')
items = soup.find_all(class_ = 'books')

for item in items:
    # item为Tag类型
    kind = item.find('h2')
    title = item.find(class_='title')
    info = item.find(class_='info')
    # print(kind + '\n' + title + '\n' + info) 
    # 以上写法报错：
    # TypeError: unsupported operand type(s) for +: 'Tag' and 'str'
    
    #print(kind, '\n', title, '\n', info)
    # 使用Tag.text方法提取文字, Tag['属性名']提取值
    print(kind.text, '\n', title.text, '\n', title['href'], '\n', info.text)
