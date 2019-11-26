# # Excel
# import requests, random, bs4
# import openpyxl

# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.title = 'douban Top250'
# sheet['A1'] = '电影名'
# sheet['B1'] = '评分'
# sheet['C1'] = '推荐语'
# sheet['D1'] = '链接'

# for x in range(10):
#     url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
#     res = requests.get(url)
#     bs = bs4.BeautifulSoup(res.text, 'html.parser')
#     bs = bs.find('ol', class_="grid_view")
#     for titles in bs.find_all('li'):
#         num = titles.find('em',class_="").text
#         title = titles.find('span', class_="title").text
#         comment = titles.find('span',class_="rating_num").text
#         url_movie = titles.find('a')['href']

#         if titles.find('span',class_="inq") != None:
#             tes = titles.find('span',class_="inq").text
#             sheet.append([title, comment, tes, url_movie])
#         else:
#             sheet.append([title, comment, '', url_movie])

# wb.save('Top250.xlsx')



# csv
# import requests, random, bs4, csv

# csv_file = open('top250.csv', 'w', newline='', encoding='utf-8')
# writer = csv.writer(csv_file)
# writer.writerow(['电影名','评分', '推荐语', '链接'])

# for x in range(10):
#     url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
#     res = requests.get(url)
#     bs = bs4.BeautifulSoup(res.text, 'html.parser')
#     bs = bs.find('ol', class_="grid_view")
#     for titles in bs.find_all('li'):
#         num = titles.find('em',class_="").text
#         title = titles.find('span', class_="title").text
#         comment = titles.find('span',class_="rating_num").text
#         url_movie = titles.find('a')['href']

#         if titles.find('span',class_="inq") != None:
#             tes = titles.find('span',class_="inq").text
#             writer.writerow([title, comment, tes, url_movie])
#         else:
#             writer.writerow([title, comment, '', url_movie])


# csv_file.close()