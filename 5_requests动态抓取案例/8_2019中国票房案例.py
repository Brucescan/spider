import requests
from lxml import etree
url = 'http://www.boxofficecn.com/boxoffice2019'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

resp =requests.get(url, headers=headers)
tree = etree.HTML(resp.content.decode())
# 切片去除最后空行
tr_list = tree.xpath('//tr[@align="left"]')[0:-1]
# print(tr_list)
for tr in tr_list:
    print(tr.xpath('./td[1]/text()'))
    # 可以加条件判断进行筛选，把空的进行删减掉
    print(tr.xpath('./td[2]/text()'))
    print(tr.xpath('./td[3]/text()'))
    print(tr.xpath('./td[4]/text()'))


resp.close()