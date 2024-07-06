import requests
from lxml import etree
import re
import time

'''
发现总页数的信息在html中，所以我们只能使用re正则去解析出来总页数
'''
# 获取页数
page_url = f'https://www.citics.com/newsite/cpzx/jrcpxxgs/dxjrcp/index.html'
headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Referer':
        'https://www.citics.com/newsite/cpzx/jrcpxxgs/dxjrcp/'
    }
resp = requests.get(page_url, headers=headers)
html = resp.content.decode()
countpage = re.search('var countPage = (.*?)//共多少页', html)


# 获取数据
for i in range(int(countpage.groups()[0])):
    page = ''
    if i > 0:
        page = '_' + str(i)
    url = f'https://www.citics.com/newsite/cpzx/jrcpxxgs/dxjrcp/index{page}.html'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Referer':
        'https://www.citics.com/newsite/cpzx/jrcpxxgs/dxjrcp/'
    }
    resp = requests.get(url, headers=headers)

    # print(resp.content.decode())
    tree = etree.HTML(resp.content.decode())
    li_list = tree.xpath('//ul[@class="list-con"]/li')
    for li in li_list:
        print(li.xpath('.//span/text()'))
    time.sleep(1)
    resp.close()
