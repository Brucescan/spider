import requests
import os.path
from lxml import etree
url = 'https://www.umei.cc/bizhitupian/diannaobizhi/'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
resp = requests.get(url, headers=headers)
# print(resp.content.decode())

tree = etree.HTML(resp.content.decode())

'''
会发现图片是懒加载
即当你不往下拉的时候默认是不加载的，会减少相应的请求,节约服务器流量
所以不能直接爬src属性，而是data-original属性
'''
img_list = tree.xpath('//div[@class="item masonry_brick"]/div/div/a/img')
# print(data_list)
if not os.path.exists('img'):
    os.makedirs('img')
for img in img_list:
    url = img.xpath('./@data-original')[0]
    alt = img.xpath('./@alt')[0]
    res = requests.get(url, headers=headers)
    with open('./img/' + alt + '.jpg','wb') as f:
        f.write(res.content)
    print(url, alt, 'over!')


resp.close()