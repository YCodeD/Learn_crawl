from gevent import monkey
# 猴子补丁
monkey.patch_all()
# 把程序变成协作式运行，就是可以帮助程序实现异步
import gevent, time, requests

start = time.time()

url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']

def crawler(url):
    r = requests.get(url)
    print(url, time.time()-start, r.status_code)

tasks_list = []

for url in url_list:
    task = gevent.spawn(crawler, url)
    # 用gevent.spawn()函数创建任务
    #gevent只能处理gevent的任务对象，不能直接调用普通函数，所以需要借助gevent.spawn()来创建任务对象。

    tasks_list.append(task)
    # 往任务列表添加任务

gevent.joinall(tasks_list)
# 执行任务列表里的所有任务，就是让爬虫开始爬取网站

end = time.time()

print(end-start)

# 用gevent实现多协程爬取的重点
# 1.定义爬取函数
# 2.用gevent.spawn()创建任务
# 3.用gevent.joinall()执行任务