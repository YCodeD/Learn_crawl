import requests, schedule
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

url = 'http://www.weather.com.cn/weather/101301104.shtml'

res = requests.get(url, headers = headers)
res.encoding = 'utf-8'

bs = BeautifulSoup(res.text, 'html.parser')
tem = bs.find('p', class_='tem')
wea = bs.find('p', class_='wea')


print('天气：' + wea.text)
print('气温：' + tem.text)