import scrapy
import bs4
from ..items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    start_urls = []

    for x in range(3):
        url = 'https://book.douban.com/top250?start='+ str(x*25)
        start_urls.append(url)

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        datas = bs.find_all('tr',class_='item')

        for data in datas:
            item = DoubanItem()
            item['title'] = data.find_all('a')[1]['title']
            item['publish'] = data.find('p', class_='pl').text
            item['score'] = data.find('span', class_='rating_nums').text
            print(item['title'])

            yield item