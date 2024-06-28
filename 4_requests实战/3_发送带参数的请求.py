import requests

# 携带参数的第一种方式
# url = 'https://so.gushiwen.cn/search.aspx?value=%E6%9D%8E%E7%99%BD&valuej=%E6%9D%8E'
# # 请求头
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Referer':
    'https://so.gushiwen.cn/search.aspx?value=%E6%9D%8E%E7%99%BD&valuej=%E6%9D%8E',
}
# # 参数
#
# # 请求
# resp = requests.get(url, headers=headers)
# print(resp.content.decode())

# 携带参数的第二种方式
url = 'https://so.gushiwen.cn/search.aspx'
# 给get传参的参数
params = {
    'value': '李白',
    'valuej': '李'
}
# 请求 携带了请求头和get参数
resp = requests.get(url, headers=headers, params=params)
print(resp.url)
# print(resp.content.decode())

resp.close()

