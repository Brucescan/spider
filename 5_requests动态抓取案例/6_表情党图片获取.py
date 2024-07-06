import requests
from lxml import etree
import os

url = 'https://qq.yh31.com/xq/wq/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

resp = requests.get(url, headers=headers)
# print(resp.content.decode())

tree = etree.HTML(resp.content.decode())
src_list = tree.xpath('//div[@class="sr"]//img/@data-src')
# 注意这里时懒加载
# print(src_list)
if not os.path.exists('img'):
    os.makedirs('img')
i = 0
for src in src_list:
    dl_resp = requests.get(src, headers=headers)
    with open('./img/' + str(i) + '.png', 'wb') as f:
        f.write(dl_resp.content)
    print('图片', i, '下载完成')
    dl_resp.close()
    i = i+1

resp.close()