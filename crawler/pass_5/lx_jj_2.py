import requests
import json

url = 'https://www.kuaidi100.com/query'

kdid = input('请输入您的单号：')
# 3713394664530

headers = {
    'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
}

params = {
    'type': 'shentong',
    'postid': kdid,
    'temp': '0.7900442742713829',
    'phone': ''
}

res = requests.get(url, params=params, headers=headers)
resjson = json.loads(res.text)
resdatas = resjson['data']

for data in resdatas:
    print(data['time'] + ' -- ' + data['context'])


# # ans
# import requests
# #调用requests模块，负责上传和下载数据

# logisticsName = input('你的快递是什么物流呀？')
# courierNum = input('你的快递单号是什么呀？')

# url = 'https://www.kuaidi100.com/query?'
# #使用get需要一个链接

# params = {
#           'type': logisticsName,
#           'postid': courierNum,
#           'temp': '0.9661515218223198',
#           'phone':''
#           }
# #将需要get的内容，以字典的形式记录在params内

# r = requests.get(url, params=params)
# #get需要输入两个参数，一个是刚才的链接，一个是params，返回的是一个Response对象
# result = r.json()

# print ('最新物流状态：'+ result['data'][0]['context'])
# #记得观察preview里面的参数哦