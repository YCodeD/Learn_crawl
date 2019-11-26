import requests
from bs4 import BeautifulSoup

url = 'https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
Tag_item = soup.find(class_='comments-area')

items = Tag_item.find_all(class_='comment-body')
print(len(items)) #1458条评论
# print(items) #1458条评论
# 打印所有评论
# i = 1
# for item in items:
#     print(str(i) + '\n')
#     print(item)
#     i += 1

for item in items:
    comment = item.find('p')
    print(comment.text)