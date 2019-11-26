import requests, schedule
import time
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# xnzeqyxhrlagfeif

def weather_spider():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    url = 'http://www.weather.com.cn/weather/101301104.shtml'

    res = requests.get(url, headers = headers)
    res.encoding = 'utf-8'

    bs = BeautifulSoup(res.text, 'html.parser')
    tem = bs.find('p', class_='tem').text
    wea = bs.find('p', class_='wea').text

    return tem, wea

acount = '1255280233@qq.com'
password = 'xnzeqyxhrlagfeif'
receiver = '1255280233@qq.com'

# password = input('请输入你的密码：')
# acount = input('请输入你的邮箱：')
# receiver = input('请输入收件人的邮箱：')

def send_email(tem, wea):
    global acount,password,receiver
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP_SSL(mailhost)
    qqmail.login(acount, password)

    content = '亲爱的，今天的天气是：' + tem + wea

    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今天天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        # 注意as_string()是一个方法，后面不能少了括号
        qqmail.sendmail(acount, receiver, message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')

    qqmail.quit()

def job():
    tem, wea = weather_spider()
    send_email(tem, wea)

# schedule.every().day.at("20:49").do(job)
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)