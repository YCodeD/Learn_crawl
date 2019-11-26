import requests
import time

session = requests.session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

url_send = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
data_send = {
    'captcha_hash': "",
    'captcha_value': "",
    'mobile': "18577322787",
    'scf': "ms"
}
sent = session.post(url_send, data=data_send, headers=headers)
print(sent.status_code)
sent_json = sent.json()
print(sent_json)
time.sleep(3)

url_get = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
data_get = {
    'mobile': "18577322787",
    'scf': "ms",
    'validate_code': input('请输入验证码：'),
    'validate_token': sent_json['validate_token']
}

res = requests.post(url_get, headers=headers, data=data_get)
print(res.status_code)