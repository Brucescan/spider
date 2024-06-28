import requests

url = 'https://ziyuan.guwendao.net/authorImg300/huangtingjian.jpg'
# 请求
resp = requests.get(url)
# print(resp.content)
with open('图片.img', 'wb') as f:
    f.write(resp.content)

print('over!')