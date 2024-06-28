import requests
from lxml import etree

'''
需求三：
获取四大名著的章节下的内容
'''

url = 'https://www.shicimingju.com/book/sanguoyanyi/1.html'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}
resp = requests.get(url, headers=headers)

tree = etree.HTML(resp.content.decode())
p_list = tree.xpath('//p')
for p in p_list:
    print(p.xpath('./text()')[0])

resp.close()