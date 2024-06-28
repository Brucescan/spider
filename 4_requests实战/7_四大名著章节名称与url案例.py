import requests
from lxml import etree

'''
需求二：
获取四大名著的章节名称和内容url
'''

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Referer':
    'https://www.shicimingju.com/bookmark/sidamingzhu.html'
}
resp = requests.get(url, headers=headers)

tree = etree.HTML(resp.content.decode())
li_list = tree.xpath('//div[@class="book-mulu"]/ul/li')
for li in li_list:
    print(li.xpath('./a/text()')[0])
    print('https://www.shicimingju.com' + li.xpath('./a/@href')[0])

resp.close()