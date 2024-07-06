import requests
import ddddocr

session = requests.session()
# 下载验证码
yzm_url = 'https://so.gushiwen.cn/RandCode.ashx'
# 发起网络请求
resp_yzm = session.get(yzm_url)
# print(resp.content)
with open('yzm.png', 'wb') as f:
    f.write(resp_yzm.content)

resp_yzm.close()
# 免费的
# 对ddddocr进行实例化
ocr = ddddocr.DdddOcr()
# 读取文件
with open('yzm.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)

# print(res)
'''
发起网络请求
'''
email = '18739878035'
pwd = 'jing040216'
url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Referer':
    'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx',
    'Content-Type':
    'application/x-www-form-urlencoded'
}
data = {
    '__VIEWSTATE':
    'XWSD0SFbqZtNE124WVQDy0AwRuIsQP8O9VFcBGP0eO7ksb1kts4y8kT09N+oRSGnPGBuiavMU+tBFcimt2sSyv9tgH7d2z27FrqeAlZQqxIN44kUWNkb9Mjhvcv2qmET5c6jCli2kslRNjNv6P/r+slIl1A=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'https://www.gushiwen.cn/',
    'email': email,
    'pwd': pwd,
    'code': res,
    'denglu': '登录',
}
resp_login = session.post(url, headers=headers, data=data)
print(resp_login.content.decode())
resp_login.close()