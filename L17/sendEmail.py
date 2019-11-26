# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header

# sender = 'from@runoon.com'
# receivers = ['1255280233@qq.com']

# message = MIMEText('Python 邮件发送测试', 'plain', 'utf-8')
# message['From'] = Header('sender', 'utf-8')
# message['To'] = Header('receiver', 'utf-8')

# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')

# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print('发送成功')
# except smtplib.SMTPException:
#     print('Error：无法发送邮件')

import smtplib
from email.mime.text import MIMEText
from email.header import Header

from_addr = '1255280233@qq.com'
password = 'rnqhdfwnoicwbaab'

to_addr = '1255280233@qq.com'

smtp_server = 'smtp.qq.com'

text = '''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''

msg = MIMEText(text, 'plain', 'utf-8')
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('python test')

#server = smtplib.SMTP()
server = smtplib.SMTP(smtp_server)
server.connect(smtp_server, 25)

server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()