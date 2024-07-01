import requests

'''
只能维护服务器端响应的cookie，而js生成的cookie只能通过逆向来进行解决
'''
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

session = requests.session()
url_1 = 'https://xueqiu.com/'

# session.get(url_1, headers=headers)

'''
统一设置headers
'''
session.headers = headers
session.get(url_1)
url_2 = 'https://xueqiu.com/statuses/hot/listV3.json?page=4&last_id=295726302'


# resp = session.get(url_2, headers=headers)
resp = session.get(url_2)
print(resp.content.decode())

resp.close()
