# 可以看到，我们点击下一页，网页页面并不会变，所以可能为异步加载的数据
import requests
import json
import re

url = 'https://53.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124000989448487670197_1719924300915&pn=2&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&dect=1&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1719924300948'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Referer': 'https://quote.eastmoney.com/center/gridlist.html'
}

resp = requests.get(url, headers=headers)

data = resp.content.decode()
# print(data)
json_data = re.search('jQuery1124000989448487670197_1719924300915\((.*?)\)', data)
# 注意search的返回结果为一个对象，需要使用groups函数取得其成员，得到的时元组，再取其第一个成员
data_dic = json.loads(json_data.groups()[0])
print(data_dic)
# 接下来就可以取数据了
resp.close()