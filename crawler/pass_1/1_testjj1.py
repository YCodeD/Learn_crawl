import requests
from bs4 import BeautifulSoup

# # 第一个小练习
# url = 'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'
# res = requests.get(url)

# bs = BeautifulSoup(res.text, 'html.parser')

# # find_ul --> <class 'bs4.element.Tag'>
# find_ul = bs.find('ul', class_='nav nav-list')

# Tag = find_ul.find_all('a')
# # print(Tag)
# # print(type(find_ul))
# for tag in Tag:
#     print(tag.text)

# 第二个小练习
url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
res = requests.get(url)

soup = BeautifulSoup(res.text,'html.parser')
# Tag --> <class 'bs4.element.ResultSet'>
items = soup.find_all('article', class_='product_pod')
#print(type(Tag))

for item in items:
    h3 = item.find('h3')
    title = h3.find('a')
    star_rating = item.find('p')
    price = item.find('p', class_='price_color')
    # print(star_rating['class'][1])
    # print(type(star_rating))
    # print(type(title))
    # print(type(price))
    print('书名'+ title['title'] + '价格' + price.text + '评分' + star_rating['class'][1])
