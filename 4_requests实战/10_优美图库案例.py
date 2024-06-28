import requests
from lxml import etree
url = 'https://www.umei.cc/bizhitupian/'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
resp = requests.get(url, headers=headers)
# print(resp.content.decode())

tree = etree.HTML(resp.content.decode())
li_list = tree.xpath('//div[@class="taotu-main"]/ul/li')

for li in li_list:
    print(li.xpath('./a/@title')[0])
    print(li.xpath('./a/@href')[0])

resp.close()