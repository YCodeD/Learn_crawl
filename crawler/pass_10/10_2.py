import smtplib
from email.mime.text import MIMEText
from email.header import Header

acount = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱：')

def send_email():
    global acount,password,receiver
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(acount, password)

    content = '亲爱的，今天的天气是：' + tem + weather

    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今天天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(acount, receiver, message.as_string)
        print('邮件发送成功')
    except:
        print('邮件发送失败')

    qqmail.quit()