import smtplib
from email.mime.text import MIMEText
from email.header import Header

acount = '1255280233@qq.com'
password = '***'
receiver = '1255280233@qq.com'

mailhost = 'smtp.qq.com'
qqmail = smtplib.SMTP_SSL()
qqmail.connect(mailhost, 465)
qqmail.login(acount, password)

content = '亲爱的，今天的天气是：' + ' tem ' + ' wea '

message = MIMEText(content, 'plain', 'utf-8')
message['From'] = Header(acount)
message['To'] = Header(receiver)
subject = '今天天气预报'
message['Subject'] = Header(subject, 'utf-8')

# qqmail.sendmail(acount, receiver, message.as_string())

try:
    qqmail.sendmail(acount, receiver, message.as_string)
    print('邮件发送成功')
except:
    print('邮件发送失败')

qqmail.quit()
