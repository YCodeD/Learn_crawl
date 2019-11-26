# #v1
# from gevent import monkey
# monkey.patch_all()
# import gevent, requests, bs4, csv
# from gevent.queue import Queue

# url = 'www.boohee.com/food/group'
# for group in range(3):
#     for page in range(3):
#         print(url + '/%s?page=%s' %(str(group+1), str(page+1)))

# url_11 = 'www.boohee.com/food/view_menu'
# for page in range(3):
#     print(url + "?page=%s" % str(page+1))


from gevent import monkey
monkey.patch_all()
import requests, bs4, csv, gevent
from gevent.queue import Queue

work = Queue()

url1 = 'http://www.boohee.com/food/group/{type}?page={page}'
for x  in range(1,4):
    for y in range(1,4):
        realurl = url1.format(type = x, page = y)
        work.put_nowait(realurl)


url2 = 'http://www.boohee.com/food/view_menu?page={page}'
for x in range(1,4):
    realurl = url2.format(page = x)
    work.put_nowait(realurl)

print(work)