import requests
# 验证码图片地址
url = 'https://so.gushiwen.cn/RandCode.ashx'

# 发起网络请求
resp = requests.get(url)
# print(resp.content)
with open('yzm.png', 'wb') as f:
    f.write(resp.content)
print('over!')
resp.close()