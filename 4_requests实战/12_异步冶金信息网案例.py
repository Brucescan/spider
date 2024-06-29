import requests
import time

'''
对于异步来说
数据来源并不是页面的url，而是异步加载的json数据
所以我们的url是json的url
'''
url = 'http://www.metalinfo.cn/json/search/list'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Referer':
    'http://www.metalinfo.cn/mi.html'
}
params = {
    'pageSize': '20',
    'current': '2',
    'resourceType': 'r_news',
    'facetFilter': {},
    'order': 'desc',
    'sort': 'sort_time',
}
for i in range(1, 5):
    params['current'] = i
    resp = requests.post(url, headers=headers, params=params)
    # print(resp.json())
    json = resp.json()
    for l in json['result']['records']:
        print(l['r_abstract_skos'])
    time.sleep(1)
    resp.close()
