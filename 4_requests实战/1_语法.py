import requests

url = 'https://www.gushiwen.cn/'
# 请求头模拟
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

# 响应的常用属性
resp = requests.get(url, headers=headers)

# 响应体的字符串类型 如果见到乱码，可以去设定编码
# resp.encoding='utf-8'
# 或者resp.encoding = resp.apparent_encoding,也行
# print(resp.text)


# 从http header中猜测的响应内容的编码方式
# print(resp.encoding)

# 响应体bytes类型   对于我们要抓取的视频，图片等数据，建议使用
# print(resp.content)
# print(resp.content.decode(‘utf-8’)) #会自动的去解析编码

# 响应状态码
# print(resp.status_code)

# 响应对应的请求头
# print(resp.request.headers)

# 响应头
# print(resp.headers)

# 非常重要，后面会重新讲
# 响应的cookie（经过了set-cookie）动作
# print(resp.cookies)

# 获取访问的url
# print(resp.url)

# 获取json()数据，得到内容为字典（如果接口响应体的格式为字典的话）
# print(resp.json())


resp.close()

