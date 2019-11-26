import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import schedule
import time

def get_menu():
    res_foods = requests.get('http://www.xiachufang.com/explore/')
    # print(res_foods.text.encode("GBK", 'ignore'))
    bs_foods = BeautifulSoup(res_foods.text,'html.parser')
    list_foods = bs_foods.find_all('div',class_='info pure-u')

    list_all = ''

    for food in list_foods:
        tag_a = food.find('a')
        name = tag_a.text[17:-13]
        URL = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        ingredients = tag_p.text[1:-1]
        list_all = list_all + ' ' + name +  ' ' + URL +  ' ' +ingredients + '\n'
        # print(list_all)
        
    return list_all

def send_email(list_all):
    acount = '1255280233@qq.com'
    password = 'xnzeqyxhrlagfeif'
    reciever = '1255280233@qq.com'

    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP_SSL()
    qqmail.connect(mailhost, 465)
    qqmail.login(acount, password)

    message = MIMEText(list_all, 'plain', 'utf-8')
    message['From'] = Header(acount)
    message['To'] = Header(reciever)
    message['Subject'] = Header('本周菜谱', 'utf-8')

    try:
        qqmail.sendmail(acount, reciever, message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')

def job():
    list_all = get_menu()
    send_email(list_all)

schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# 输出系统编码
# import sys
# print(sys.getdefaultencoding())

# 答案
# import requests
# import smtplib
# import schedule
# import time
# from bs4 import BeautifulSoup
# from email.mime.text import MIMEText
# from email.header import Header

# account = input('请输入你的邮箱：')
# password = input('请输入你的密码：')
# receiver = input('请输入收件人的邮箱：')

# def recipe_spider():
#     res_foods = requests.get('http://www.xiachufang.com/explore/')
#     bs_foods = BeautifulSoup(res_foods.text,'html.parser')
#     list_foods = bs_foods.find_all('div',class_='info pure-u')
#     list_all = ''
#     num=0
#     for food in list_foods:
#         num=num+1
#         tag_a = food.find('a')
#         name = tag_a.text.strip()
#         url = 'http://www.xiachufang.com'+tag_a['href']
#         tag_p = food.find('p',class_='ing ellipsis')
#         ingredients = tag_p.text.strip()
#         food_info = '''
#         序号: %s
#         菜名: %s
#         链接: %s
#         原料: %s
#         '''%(num,name,url,ingredients)
#         list_all=list_all+food_info
#     return(list_all)

# def send_email(list_all):
#     global account,password,receiver
#     mailhost='smtp.qq.com'
#     qqmail = smtplib.SMTP()
#     qqmail.connect(mailhost,25)
#     qqmail.login(account,password)
#     content= '亲爱的，本周的热门菜谱如下'+list_all
#     message = MIMEText(content, 'plain', 'utf-8')
#     subject = '周末吃个啥'
#     message['Subject'] = Header(subject, 'utf-8')
#     try:
#         qqmail.sendmail(account, receiver, message.as_string())
#         print ('邮件发送成功')
#     except:
#         print ('邮件发送失败')
#     qqmail.quit()

# def job():
#     print('开始一次任务')
#     list_all = recipe_spider()
#     send_email(list_all)
#     print('任务完成')

# schedule.every().friday.at("18:00").do(job)#部署每周三的13：15执行函数的任务

# while True:
#     schedule.run_pending()
#     time.sleep(1)