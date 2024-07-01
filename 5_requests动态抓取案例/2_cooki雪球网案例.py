import requests

# headers = {
#     'User-Agent':
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
#     'Referer':
#     'https://xueqiu.com/',
#     'Cookie':
#     'acw_tc=276077ad17197506574775466eb06f2d8359bc75c18d7243c8da3fff64e8ea; xq_a_token=483932c5fb313ca4c93e7165a31f179fb71e1804; xqat=483932c5fb313ca4c93e7165a31f179fb71e1804; xq_r_token=f3a274495a9b8053787677ff7ed85d1639c6e3e0; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcyMTQzNjcyOSwiY3RtIjoxNzE5NzUwNjUxMjIyLCJjaWQiOiJkOWQwbjRBWnVwIn0.gXCHDy4qiAhsUAMWqeOsFmjmJT9uYusdgsMzpb6TVJgWy5JwjL0eVueAl5iGhQR6g1ZZUOSHXYy9OzzHzRQKob78gjqDcYP0SF7-LXdF16MNS1T-c6MyVLznw5CM3X39IUpcRw_nhHB729XudiwsWPI9b0lqJB5rjMPVAPgkSgmtCeCViXfj5AoezkWcI4WuK50NVc0zwxT_N90grpaGjmhO6JmHo2Fpgz3N-8_MkaNai-1elra0MIu79lotT4d1dhKLJP0mqq18aTjPH5Bu3oIF2tNHO6z0xTAHPflkzw-Lqv6adYKTRA4wuS8Z64fyS0PWw2ZxJwWNYJ3oyciAyw; cookiesu=801719750657485; u=801719750657485; Hm_lvt_1db88642e346389874251b5a1eded6e3=1719750659; device_id=30e9d2ed0cb9af2622bc8704f17b2a8a; smidV2=202406302030582f62d3f776f00ce3a17a2470d09a99cd008cd40109b192ef0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1719751692; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=bm0lXnq7/t//rX8RHgnNzEhL09Vhe3NfWF7U2Puk3ABLT/m2PrB9KMzVcmdWKnFr9LSvcWTZachjZLdDkoU9bg%3D%3D'
# }
#
# url = 'https://xueqiu.com/statuses/hot/listV3.json?page=4&last_id=295726302'
#
# resp = requests.get(url, headers=headers)
# print(resp.content.decode())

'''
获取cookie并携带
'''

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}
url_1 = 'https://xueqiu.com/'

'''
获取访问首页时响应的cookie
'''

resp = requests.get(url_1, headers=headers)
cookies = dict(resp.cookies)
# 第二种方式
# cookies = requests.utils.dict_from_cookiejar(resp.cookies)
# print(cookies)
url_2 = 'https://xueqiu.com/statuses/hot/listV3.json?page=4&last_id=295726302'

# 手动携带cookie进行访问
res = requests.get(url_2, headers=headers ,cookies=cookies)
print(res.content.decode())

resp.close()