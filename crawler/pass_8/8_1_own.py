import requests
url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
headers = {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
data = {
    'log': 'spiderman',
    'pwd': 'crawler334566',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work',
    'testcookie': '1'
}

res = requests.post(url, headers=headers, data=data)
cookies = res.cookies

url_com = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'

data1 = {
    'comment': input('请输入你的评论'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
}

res_com = requests.post(url_com, headers=headers, data=data1, cookies=cookies)
print(res_com)