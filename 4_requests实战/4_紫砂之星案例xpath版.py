import requests
from lxml import etree

# url
url = 'http://zishazx.com/product'

# 请求头
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Referer':
    'http://zishazx.com/product',
}
# 携带参数
params = {
    'page': '1',
    'size_id': '1',
    'volum_id': '3',
    'price_id': '2',
    'category_id': '0',
    'prize_id': '1',
    'pug_id': '1',
}
# 发送请求
# resp = requests.get(url, headers=headers, params=params)
# print(resp.content.decode())
# 解析数据
# with open('zszx.html','w',encoding='utf-8') as f:
#     f.write(resp.content.decode())

with open('zszx.html','r',encoding='utf-8') as f:
    html = f.read()
# print(html)
tree = etree.HTML(html)
# 数据提取
li_list = tree.xpath('//ul[@class="h_list clearfix J_product_fcont"]/li')
# print(li_list
for li in li_list:
    print(li.xpath('./p[@class="name"]/text()')[0])
    print(li.xpath('./p[@class="p_no"]/text()')[0])
# resp.close()
