import requests

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# #res是一个对象，属于resquests.models.Reaponse类
# #Response对象常用的四个属性：
# #  response.status_code    检查请求是否成功    200--请求成功
# #  response.content        把response对象转换为二进制数据    适用图片、音频、视频的下载
# #  response.text           把response对象转换为字符串数据    对象的内容以字符串的形式返回，适用于文字、网页源代码的下载
# #  response.encoding       定义response对象编码
print(type(res))



