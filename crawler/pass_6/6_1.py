import csv

# 写入数据
# csv_file = open('demo.csv', 'w', newline = '', encoding = 'utf-8')
# write = csv.writer(csv_file)
# write.writerow(['豆瓣', '评分'])
# write.writerow(['流浪地球', '8.0'])
# write.writerow(['复仇者联盟4', '9.0'])

# 读数据
csv_file = open('demo.csv', 'r', newline = '', encoding='utf-8')
read = csv.reader(csv_file)
for item in read:
    print(item)