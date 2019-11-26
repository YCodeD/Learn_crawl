import requests

url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'

commentid = ''


#请求头
heards = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

for i in range(2):
    params = {
        'g_tk':'5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'GB2312',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
        'cid': '205360772',
        'reqtype': '2',
        'biztype': '1',
        'topid': '102065756',
        'cmd': '8',
        'needmusiccrit': '0',
        'pagenum': str(i),
        'pagesize': '25',
        'lasthotcommentid': commentid,
        'domain': 'qq.com',
        'ct': '24',
        'cv': '10101010'
    }


    res = requests.get(url,params=params)
    comment_json = res.json()

    #循环可以依照参考进行优化
    for j in range(24):
        print(comment_json['comment']['commentlist'][j]['rootcommentcontent'])


    commentid = comment_json['comment']['commentlist'][24]['rootcommentid']

#参考
# import requests
# # 引用requests模块
# url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
# commentid = ''
# # 设置一个初始commentid
# for x in range(5):
    
#     params = {
#     'g_tk':'5381',
#     'loginUin':'0',
#     'hostUin':'0',
#     'format':'json',
#     'inCharset':'utf8',
#     'outCharset':'GB2312',
#     'notice':'0',
#     'platform':'yqq.json',
#     'needNewCode':'0',
#     'cid':'205360772',
#     'reqtype':'2',
#     'biztype':'1',
#     'topid':'102065756',
#     'cmd':'8',
#     'needcommentcrit':'0',
#     'pagenum':str(x),
#     'pagesize':'25',
#     'lasthotcommentid':commentid,
#     'domain':'qq.com',
#     'ct':'24',
#     'cv':'101010  '
#     }
#     # 将参数封装为字典，其中pagenum和lastcommentid是特殊的变量
#     res_comment = requests.get(url,params=params)
#     # 调用get方法，下载评论列表
#     json_comment = res_comment.json()
#     # 使用json()方法，将response对象，转为列表/字典
#     list_comment = json_comment['comment']['commentlist']
#     # 一层一层地取字典，获取评论列表
#     for comment in list_comment:
#     # list_comment是一个列表，comment是它里面的元素
#         print(comment['rootcommentcontent'])
#         # 输出评论
#     commentid = list_comment[24]['commentid']
#     # 将最后一个评论的id赋值给comment，准备开始下一次循环