import requests


# API接口，返回格式为json
# api_url = "http://www.zdopen.com/ShortProxy/GetIP/?api=202406301717506573&akey=81d7e21f978ccc95&count=2&fitter=2&timespan=0&type=3"
#
# # API接口返回的ip
# proxy_ip = requests.get(api_url).json()['data']['proxy_list']
#
# print(proxy_ip)
url = 'http://httpbin.org/ip'

proxies = {
    "http": "http://171.15.173.79:15537",
    "https": "http://171.15.173.79:15537"
}
resp = requests.get(url, proxies=proxies)

print(resp.content.decode())
resp.close()