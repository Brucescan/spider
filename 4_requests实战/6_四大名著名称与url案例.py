import requests
from lxml import etree

'''
需求一：
获取四大名著的书名和url
'''

url = 'https://www.shicimingju.com/bookmark/sidamingzhu.html'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Referer':
    'https://www.shicimingju.com/book/'
}
resp = requests.get(url, headers=headers)

tree = etree.HTML(resp.content.decode())
# 返回超链接
a_list = tree.xpath('//div[@class="book-item"]/h3/a')
# print(a_list)
for a in a_list:
    # 获取书的超链接
    print(a.xpath('./text()')[0])
    # 拼接完整的超链接
    print('https://www.shicimingju.com' + a.xpath('./@href')[0])
# print(resp.content.decode())



resp.close()