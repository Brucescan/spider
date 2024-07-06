import requests

cookie_url = 'https://www.xiaohua.com/Handler/Login.ashx'
headers = {
   ''
}
'''
网站进不去了，操
'''
data = {
    'username': '',
    'password': ''
}
session = requests.session()
# 只是用来登录获取服务器给的cookie
session.post(cookie_url, headers=headers, data=data)
# 获取数据的url
url = ''
# 此时session已经携带了cookie，所以不需要传递cookie参数了
resp = session.get(url, headers=headers)

print(resp.content.decode())
resp.close()